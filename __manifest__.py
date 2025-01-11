# -*- coding: utf-8 -*-

{
    'name': 'Subscription Management',
    'version': '17.0.2.1.2',
    'category': 'Sales',
    'summary': 'Subscription Package Management Module For Odoo17 Community',
    'description': 'Subscription Package Management Module specifically '
                   'designed for Odoo 17 Community edition. '
                   'This module aims to enhance the subscription '
                   'management capabilities within the Odoo platform, '
                   'providing users with advanced features and '
                   'functionalities for efficiently handling subscription '
                   'packages in the community version of Odoo 17.',
    'author': 'Cybrosys Techno solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'sale_management'],
    'data': [
        'security/subscription_package_groups.xml',
        'security/ir.model.access.csv',
        'data/uom_demo_data.xml',
        'data/subscription_package_stop_data.xml',
        'data/subscription_stage_data.xml',
        'data/mail_subscription_renew_data.xml',
        'data/ir_cron_data.xml',
        'data/ir_sequence.xml',
        'views/subscription_package_views.xml',
        'views/product_template_views.xml',
        'views/subscription_package_plan_views.xml',
        'views/subscription_stage_views.xml',
        'views/subscription_package_stop_views.xml',
        'views/mail_activity_views.xml',
        'views/res_partner_views.xml',
        'views/recurrence_period_views.xml',
        'views/sale_order_views.xml',
        'views/product_product_views.xml',
        'views/gym_attendance_views.xml',
        'report/subscription_report_view.xml',
        'report/id_card_templates.xml',
        'report/subscription_label_report2.xml',
        'wizard/subscription_close_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
