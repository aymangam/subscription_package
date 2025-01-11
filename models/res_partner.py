# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """Inherited res partner model"""
    _inherit = 'res.partner'

    is_active_subscription = fields.Boolean(string="Active Subscription",
                                            default=False,
                                            help='Is Subscription is active')
    subscription_product_line_ids = fields.One2many(
        'subscription.package.product.line', 'res_partner_id',
        ondelete='restrict', string='Products Line',
        help='Subscription product')

    def _valid_field_parameter(self, field, name):
        """
        Validate field parameters, allowing custom handling for 'ondelete'
        """
        if name == 'ondelete':
            return True
        return super(ResPartner,
                     self)._valid_field_parameter(field, name)
