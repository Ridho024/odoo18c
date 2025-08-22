{
    'name': "Stock Valuation for Odoo Community",
    'summary': "Stock Valuation for Odoo Community Edition Plus",
    'description': """
Long description of module's purpose
    """,
    'author': "Ridho024",
    'website': "https://www.yourcompany.com",
    'category': 'Accounting',
    'version': '1.0',
    'depends': ['base', 'account', 'stock'],
    'data': [
        'data/stock_valuation_account.xml',
        'views/res_config_settings_views.xml',
        'views/product_category_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

