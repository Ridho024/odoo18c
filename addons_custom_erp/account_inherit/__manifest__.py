{
    'name': "Inventory Valuation and Payment",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Accounting',
    'version': '0.1',
    'depends': ['base', 'account', 'stock', 'account_payment', 'om_account_accountant', 'om_account_asset'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

