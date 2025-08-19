# -*- coding: utf-8 -*-
# from odoo import http


# class StockAccountCePlus(http.Controller):
#     @http.route('/stock_account_ce_plus/stock_account_ce_plus', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_account_ce_plus/stock_account_ce_plus/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_account_ce_plus.listing', {
#             'root': '/stock_account_ce_plus/stock_account_ce_plus',
#             'objects': http.request.env['stock_account_ce_plus.stock_account_ce_plus'].search([]),
#         })

#     @http.route('/stock_account_ce_plus/stock_account_ce_plus/objects/<model("stock_account_ce_plus.stock_account_ce_plus"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_account_ce_plus.object', {
#             'object': obj
#         })

