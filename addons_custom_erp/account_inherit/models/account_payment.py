from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_post(self): # Nanti lu ganti jadi action validate
        res = super().action_post()
        for payment in self:
            if payment.state != 'posted':
                continue

            # Skip jika journal entry sudah ada
            existing_move = self.env['account.move'].search([('ref', '=', f'Auto Payment {payment.name}')], limit=1)
            if existing_move:
                continue

            # Tentukan akun debit dan kredit
            if payment.payment_type == 'outbound':
                # Pembayaran ke supplier (keluar uang dari bank)
                debit_account = payment.destination_account_id.id  # Payable
                credit_account = payment.journal_id.default_account_id.id  # Bank
            elif payment.payment_type == 'inbound':
                # Pembayaran dari customer (masuk uang ke bank)
                debit_account = payment.journal_id.default_account_id.id  # Bank
                credit_account = payment.destination_account_id.id  # Receivable
            else:
                raise UserError(_('Unsupported payment type'))

            # Buat journal entry
            move_vals = {
                'ref': f'Auto Payment {payment.name}',
                'journal_id': payment.journal_id.id,
                'date': payment.date,
                'line_ids': [
                    (0, 0, {
                        'name': payment.name,
                        'account_id': debit_account,
                        'debit': payment.amount,
                        'credit': 0.0,
                        'partner_id': payment.partner_id.id,
                    }),
                    (0, 0, {
                        'name': payment.name,
                        'account_id': credit_account,
                        'debit': 0.0,
                        'credit': payment.amount,
                        'partner_id': payment.partner_id.id,
                    })
                ]
            }
            move = self.env['account.move'].create(move_vals)
            move.action_post()

            # Tambahkan link balik ke payment jika perlu
            # payment.write({'custom_journal_entry_id': move.id})  # Opsional

        return res