# -*- coding: utf-8 -*-
{
    'name': "Application de Gestion immobilière",

    'summary': """Gérer vos biens immobiliers avec cette application""",

    'author': "MTechniix",
    'website': "https://www.mtechniix.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/acheteur.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tags.xml',
        'views/menus.xml',
        'reports/estate_property_report.xml',
    ],
}
