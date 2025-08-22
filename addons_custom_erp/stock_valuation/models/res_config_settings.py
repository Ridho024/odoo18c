from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    automatic_accounting = fields.Boolean(string='Automatic Accounting', 
                                          config_parameter='stock_valuation.automatic_accounting')
    
    # General
    income_account_id = fields.Many2one('account.account', string='Income Account', 
                                        config_parameter='stock_valuation.income_account_id', 
                                        domain=['&', ('deprecated', '=', False), ('account_type', 'not in', ('asset_receivable', 
                                                                                                             'liability_payable', 
                                                                                                             'asset_cash',
                                                                                                             'liability_credit_card', 
                                                                                                             'off_balance'))], 
                                        default=lambda self: self.env.ref('account.1_l10n_id_41000010', raise_if_not_found=False).id
                                        )
    
    expense_account_id = fields.Many2one('account.account', string='Expense Account', 
                                         config_parameter='stock_valuation.expense_account_id', 
                                         domain=['&', ('deprecated', '=', False), ('account_type', 'not in', ('asset_receivable', 
                                                                                                              'liability_payable', 
                                                                                                              'asset_cash', 
                                                                                                              'liability_credit_card', 
                                                                                                              'off_balance'))],
                                         default=lambda self: self.env.ref('account.1_l10n_id_69000000', raise_if_not_found=False).id
                                         )
    
    # WIP
    wip_account_id = fields.Many2one('account.account', string='WIP Account', 
                                     config_parameter='stock_valuation.wip_account_id',
                                     default=lambda self: self.env.ref('stock_valuation.default_wip_account', raise_if_not_found=False).id
                                     )
    
    wip_overhead_account_id = fields.Many2one('account.account', string='WIP Overhead Account', 
                                              config_parameter='stock_valuation.wip_overhead_account_id',
                                              default=lambda self: self.env.ref('stock_valuation.default_wip_overhead_account', raise_if_not_found=False).id
                                              )
     
    # Automatic Accounting
    stock_valuation_account_id = fields.Many2one('account.account', string='Stock Valuation Account', 
                                                 config_parameter='stock_valuation.stock_valuation_account_id', 
                                                 domain=[('deprecated', '=', False)],
                                                 default=lambda self: self.env.ref('stock_valuation.default_stock_valuation_account', raise_if_not_found=False).id
                                                 )
    
    stock_input_account_id = fields.Many2one('account.account', string='Stock Input Account', 
                                             config_parameter='stock_valuation.stock_input_account_id', 
                                             domain=[('deprecated', '=', False)],
                                             default=lambda self: self.env.ref('stock_valuation.default_stock_input_account', raise_if_not_found=False).id)
    
    stock_output_account_id = fields.Many2one('account.account', string='Stock Output Account', 
                                              config_parameter='stock_valuation.stock_output_account_id',
                                              default=lambda self: self.env.ref('stock_valuation.default_stock_output_account', raise_if_not_found=False).id
                                              )
    
    production_account_id = fields.Many2one('account.account', string='Production Account', 
                                            config_parameter='stock_valuation.production_account_id', 
                                            domain=[('deprecated', '=', False)],
                                            default=lambda self: self.env.ref('stock_valuation.default_stock_production_account', raise_if_not_found=False).id
                                            )
    
    stock_journal_id = fields.Many2one('account.journal', string='Stock Journal', 
                                       config_parameter='stock_valuation.stock_journal_id',
                                       default=lambda self: self.env.ref('account.1_inventory_valuation', raise_if_not_found=False).id
                                       )
