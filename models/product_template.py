# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    """Inherited product template model"""
    _inherit = "product.template"

    is_subscription = fields.Boolean(string='Is Subscription', default=False,
                                     help='Indicates whether the product is '
                                          'associated with a subscription '
                                          'or not.')
    subscription_plan_id = fields.Many2one('subscription.package.plan',
                                           string='Subscription Plan',
                                           help='Select the subscription plan '
                                                'associated with this record.')
