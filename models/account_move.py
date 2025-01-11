# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountMove(models.Model):
    """Inherited sale order model"""
    _inherit = "account.move"

    is_subscription = fields.Boolean(string='Is Subscription', default=False,
                                     help='Is subscription')
    subscription_id = fields.Many2one('subscription.package',
                                      string='Subscription',
                                      help='Choose subscription package')

    @api.model_create_multi
    def create(self, vals_list):
        """ It displays subscription in account move """
        for rec in vals_list:
            so_id = self.env['sale.order'].search(
                [('name', '=', rec.get('invoice_origin'))])
            if so_id.is_subscription is True:
                so_id.subscription_id.start_date = so_id.subscription_id.next_invoice_date
                new_vals_list = [{'is_subscription': True,
                                  'subscription_id': so_id.subscription_id.id}]
                vals_list[0].update(new_vals_list[0])
        return super().create(vals_list)
