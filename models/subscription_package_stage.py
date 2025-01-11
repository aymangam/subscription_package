# -*- coding: utf-8 -*-
from odoo import models, fields


class SubscriptionPackageStage(models.Model):
    _name = "subscription.package.stage"
    _description = "Subscription Package Stages"
    _rec_name = 'name'

    name = fields.Char(string='Stage Name', required=True,
                       help=' Enter a descriptive name for the stage')
    sequence = fields.Integer('Sequence', help="Determine the display order",
                              index=True)
    condition = fields.Text(string='Conditions',
                            help='Use this field to provide detailed '
                                 'information about the conditions')
    is_fold = fields.Boolean(string='Folded in Kanban',
                             help="This stage is folded in the kanban view "
                                  "when there are no records in that stage "
                                  "to display.")
    category = fields.Selection([('draft', 'Draft'),
                                 ('progress', 'In Progress'),
                                 ('paused', 'Paused'),
                                 ('closed', 'Closed')],
                                readonly=False, default='draft',
                                help='Choose the appropriate category from'
                                     ' the available options.')
