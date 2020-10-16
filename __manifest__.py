# -*- coding: utf-8 -*-
{
    'name': 'Ganaderia',
    'version': '12.0.1.0.1',
    'summary': """Modulo para gestionar registros de ganado, propietarios, identificando sus caracteristicas principales""",
    'category': 'Cobros',
    'author': 'Santiago Betancur Villegas',
    'company': 'Grupo Umanizales profundización II ',
    'website': 'https://www.umanizales.com',
    'description': """Realizar manipulación de cobros y todos sus procesos financieros""",
    'depends': ['mass_mailing'],
    'data': [
        'security/ganaderia_security.xml',
        'security/ir.model.access.csv',
        'views/ganaderia_ganado_view.xml',
        'views/ganaderia_ganadero_view.xml',
        'views/ganaderia_finca_view.xml',
        'views/ganaderia_parametricas_view.xml',
        'views/ganaderia_menu.xml',
        #'views/captcha_views.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}