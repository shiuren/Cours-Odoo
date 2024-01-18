{
    'name' : 'Geek Gaming', 
    'summary' : 'Joueur Internationnal',
    'author': "MTechniix",
    'website': "https://www.mtechniix.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','estate','hr','project','mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/team.xml',
        'views/player.xml',
        'views/offer.xml',
        'views/menu.xml',
        'views/inherite_estate.xml',
        'security/report_security.xml'
    ],
}