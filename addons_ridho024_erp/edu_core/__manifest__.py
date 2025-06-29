# -*- coding: utf-8 -*-
{
    'name': "Education Core",

    'summary': "Core functionalities for Education Management",

    'description': """
    This module provides the core functionalities for managing educational institutions,
    """,

    'author': "Ridho024",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '0.1',

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/mail_activity_schedule_views.xml',
        'views/res_partner_inherit_views.xml',
        'views/std_attendance_views.xml',
        'views/std_attendance_menu_views.xml',
    ],

    'demo': [],
}

