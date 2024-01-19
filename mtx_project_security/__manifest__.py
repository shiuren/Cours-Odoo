# -*- coding: utf-8 -*-
{
    'name': "mtx_project_security",

    'summary': """
        """,

    'description': """
       
    """,

    'author': "Mtechniix",
    'website': "https://www.metchniix.com",

    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/project_security.xml',
        'security/group_readonly.xml',
        'views/inherit_project_task.xml',
    ],
    
}
