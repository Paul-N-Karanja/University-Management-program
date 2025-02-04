# -*- coding: utf-8 -*-
{
    'name': "University Management",

    'summary': "Aid in the management of a schools day to day operations",

    'description': """ """,

    'author': "Paul Karanja",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management/School',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"mail"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        "views/student_add_views.xml",
        "views/student_view_views.xml",
        "views/university_menus.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application":True,
    "license":"LGPL-3"
}

