from odoo import models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super().button_validate()
        for move in self.move_lines:
            move._create_stock_valuation_journal_entry()
        return res
