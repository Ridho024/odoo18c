from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = 'product.category'

    automatic_accounting = fields.Boolean(
        string='Automatic Accounting',
        default=lambda self: self.env['ir.config_parameter'].sudo().get_param('stock_valuation.automatic_accounting', default=False)
    )
    
    property_account_income_categ_id = fields.Many2one(default=lambda self: self.env['ir.config_parameter'].sudo().get_param('stock_valuation.income_account_id', default=False))
    property_account_expense_categ_id = fields.Many2one(
        default=lambda self: self.env['ir.config_parameter'].sudo().get_param('stock_valuation.expense_account_id', default=False)
    )
    
    property_stock_valuation_account_id = fields.Many2one(default=lambda self: self.env['ir.config_parameter'].sudo().get_param('stock_valuation.stock_valuation_account_id', default=False))
    property_stock_journal = fields.Many2one(default=lambda self: self.env['ir.config_parameter'].sudo().get_param('stock_valuation.stock_journal_id', default=False))
    property_stock_account_input_categ_id = fields.Many2one(default=lambda self: self.env['ir.config_parameter'].sudo().get_param('stock_valuation.stock_input_account_id', default=False))
    property_stock_account_output_categ_id = fields.Many2one(default=lambda self: self.env['ir.config_parameter'].sudo().get_param('stock_valuation.stock_output_account_id', default=False))