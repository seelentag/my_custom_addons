{
    'name': 'Custom Project',
    'version': '1.0',
    'summary': 'Adds a custom project model with chatter.',
    'author': 'Your Name',
    'depends': ['base', 'mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_project_views.xml',
    ],
    'installable': True,
    'application': True,
}
