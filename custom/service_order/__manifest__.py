# -*- coding: utf-8 -*-
{
    'name' : 'Service Order',
    'description':"""
        Service Order
        =======================================
        Módulo criado com o intuito de oferecer uma opção funcional para 
        Assistências Técnicas de qualquer ramo.
    """,
    'version' : '1.0',
    'category': 'Services',
    'depends' : ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/service_order.xml',
        'views/service_order_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
