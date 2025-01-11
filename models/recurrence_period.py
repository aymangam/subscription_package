# -*- coding: utf-8 -*-
from odoo import fields, models


class RecurrencePeriod(models.Model):
    """This class is used to create new model recurrence period"""
    _name = "recurrence.period"
    _description = "Recurrence Period "

    name = fields.Char(string="Name",
                       help='The name of the recurrence period. Enter a '
                            'descriptive name for the period.')
    duration = fields.Float(string="Duration",
                            help='The duration associated with this record. '
                                 'Enter the duration value.')
    unit = fields.Selection([('hours', 'hours'),
                             ('days', 'Days'), ('weeks', 'Weeks'),
                             ('months', 'Months'), ('years', 'Years')],
                            string='Unit',
                            help='Select the unit of time associated with this '
                                 'record. Choose from the available options.')
