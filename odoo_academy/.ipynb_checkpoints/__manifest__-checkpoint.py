# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage Training""",
    
    'description': """
        Academy Module to mange Training
        - Courses
        - Sessions
        - Attenddess
    """,
    
    'author': 'Darren O',
    
    'website': 'https://www.methodandmode.co',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml'
        'security/ir.model.access.csv'
        
    ],
    
    'demo': [
        'demo/academy_demo.xml',
        
    ],
        #Add license to remove License Warning
    'license': 'OPL-1'
}