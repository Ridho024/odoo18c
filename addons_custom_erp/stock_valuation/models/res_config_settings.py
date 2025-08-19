from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    automatic_accounting = fields.Boolean(string='Automatic Accounting', config_parameter='stock_valuation.automatic_accounting')
    
    # General
    income_account_id = fields.Many2one('account.account', string='Income Account', config_parameter='stock_valuation.income_account_id')
    expense_account_id = fields.Many2one('account.account', string='Expense Account', config_parameter='stock_valuation.expene_account_id')
    
    # WIP
    wip_account_id = fields.Many2one('account.account', string='WIP Account', config_parameter='stock_valuation.wip_account_id')
    wip_overhead_account_id = fields.Many2one('account.account', string='WIP Overhead Account', config_parameter='stock_valuation.wip_overhead_account_id')
    
    # Automatic Accounting
    stock_valuation_account_id = fields.Many2one('account.account', string='Stock Valuation Account', config_parameter='stock_valuation.stock_valuation_account_id')
    stock_input_account_id = fields.Many2one('account.account', string='Stock Input Account', config_parameter='stock_valuation.stock_input_account_id')
    stock_output_account_id = fields.Many2one('account.account', string='Stock Output Account', config_parameter='stock_valuation.stock_output_account_id')
    production_account_id = fields.Many2one('account.account', string='Production Account', config_parameter='stock_valuation.production_account_id')
    stock_journal_id = fields.Many2one('account.journal', string='Stock Journal', config_parameter='stock_valuation.stock_journal_id')
     