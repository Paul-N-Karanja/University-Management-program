# -*- coding: utf-8 -*-
{
    'name': "University Management Program",

    'summary': "Assist with day to day tasks done in managing a university",

    "license":"LGPL-3",

    'author': "Paul Karanja",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '17.0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/menu.xml",
    ],
    "application": True,
}

