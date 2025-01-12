# -*- coding: utf-8 -*-

from odoo import models, fields


class SubscriptionClose(models.TransientModel):
    _name = 'subscription.close'
    _description = 'Subscription Close Wizard'

    close_reason_id = fields.Many2one('subscription.package.stop',
                                      string='Close Reason',
                                      help='Add Subscription Package '
                                           'Close Reason')
    closed_by = fields.Many2one('res.users', string='Closed By',
                                default=lambda self: self.env.user,
                                help='Choose  Subscription Package '
                                     'Closed Person')
    close_date = fields.Date(string='Closed On',
                             default=lambda self: fields.Date.today(),
                             help='Add Subscription Package Closed Date')

    def button_submit(self):
        self.ensure_one()
        this_sub_id = self.env.context.get('active_id')
        sub = self.env['subscription.package'].search(
            [('id', '=', this_sub_id)])
        sub.is_closed = True
        sub.close_reason_id = self.close_reason_id
        sub.closed_by = self.closed_by
        sub.close_date = self.close_date
        stage = (self.env['subscription.package.stage'].search([
            ('category', '=', 'closed')]).id)
        values = {'stage_id': stage, 'is_to_renew': False}
        sub.write(values)
        for lines in sub.sale_order_id.order_line.filtered(
                lambda x: x.product_template_id.is_subscription == True):
            lines.qty_invoiced = lines.product_uom_qty
            lines.qty_to_invoice = 0
