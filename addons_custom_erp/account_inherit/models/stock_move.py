from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    def _create_stock_valuation_journal_entry(self):
        for move in self:
            product = move.product_id
            if product.valuation != 'manual':
                continue

            if move.location_id.usage == 'internal' and move.location_dest_id.usage != 'internal':
                # Barang keluar
                debit_account = product.categ_id.property_stock_output_account_id.id
                credit_account = product.categ_id.property_stock_valuation_account_id.id
            elif move.location_id.usage != 'internal' and move.location_dest_id.usage == 'internal':
                # Barang masuk
                debit_account = product.categ_id.property_stock_valuation_account_id.id
                credit_account = product.categ_id.property_stock_input_account_id.id
            else:
                continue

            journal = self.env['account.journal'].search([('type', '=', 'general')], limit=1)
            move.env['account.move'].create({
                'ref': f'Stock Valuation {move.name}',
                'journal_id': journal.id,
                'date': fields.Date.today(),
                'line_ids': [
                    (0, 0, {
                        'name': move.name,
                        'account_id': debit_account,
                        'debit': move.product_id.standard_price * move.product_uom_qty,
                        'credit': 0.0,
                    }),
                    (0, 0, {
                        'name': move.name,
                        'account_id': credit_account,
                        'debit': 0.0,
                        'credit': move.product_id.standard_price * move.product_uom_qty,
                    })
                ]
            })