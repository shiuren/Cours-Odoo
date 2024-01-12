# -*- coding: utf-8 -*-
{
    'name': "custome house",


    'description': """
        Long description of module's purpose
    """,

    'author': "My MTechniix",
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
        'views/house.xml',
        'views/house_type.xml',
        'views/house_tag.xml',
        'views/property_offer.xml',
        'views/res_user.xml',
        'views/menu.xml',
    ],
   
}
