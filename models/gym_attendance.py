from odoo import models, fields, api
from odoo.exceptions import UserError


class GymAttendance(models.Model):
    _name = 'gym.attendance'
    _description = 'Gym Attendance'
    _rec_name = 'subscription_id'

    subscription_id = fields.Many2one('subscription.package', required=1, string='Subscription', domain=[('stage_id', '=', 2)])
    partner_id = fields.Many2one('res.partner', string='Customer', related='subscription_id.partner_id')
    attendance_date = fields.Datetime('Attendance Date', default=fields.Datetime.now())
    hours_spent = fields.Float('Hours Spent')
    present = fields.Boolean('Present', default=False)
    attendance_day = fields.Date('Day', default=fields.Date.today)

    @api.model_create_multi
    def create(self, values):
        for vals in values:
            existing_attendance = self.env['gym.attendance'].search([
                ('subscription_id', '=', vals.get('subscription_id')),
                ('attendance_day', '=', vals.get('attendance_day')),
            ])
            if existing_attendance:
                raise UserError("هذا المتدرب قد حضر اليوم بالفعل!")
        return super(GymAttendance, self).create(values)


    def write(self, values):
        for rec in self:
            for vlas in values:
                existing_attendance = rec.env['gym.attendance'].search([
                    ('subscription_id', '=', vlas.get('subscription_id')),
                    ('attendance_day', '=', vlas.get('attendance_day')),
                ])
                if existing_attendance:
                    raise UserError("لا يمكن تعديل الحضور في نفس اليوم!")

            return super(GymAttendance, self).write(values)
