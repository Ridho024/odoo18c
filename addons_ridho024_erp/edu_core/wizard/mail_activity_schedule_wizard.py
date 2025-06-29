from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MailActivitySchedule(models.TransientModel):
    _inherit = 'mail.activity.schedule'

    start_time = fields.Float(string='Start Time', default=8.0, digits=(2, 2))
    end_time = fields.Float(string='End Time', default=17.0, digits=(2, 2))
    
    @api.constrains('start_time', 'end_time')
    def _check_time_not_negative(self):
        for rec in self:
            if rec.start_time < 0 or rec.end_time < 0:
                raise ValidationError("Start and end times must be non-negative.")
            if rec.start_time >= rec.end_time:
                raise ValidationError("Start time must be less than end time.")
    
    def action_schedule(self):
        """Override to set default start and end times."""
        self.ensure_one()
        res = super().action_schedule()
        
        activity = self.env['mail.activity']
        for wizard in self:
            
            domain = [
                ('res_model', '=', wizard.res_model),
                ('res_id', '=', wizard.res_id),
                ('activity_type_id', '=', wizard.activity_type_id.id),
                ('user_id', '=', wizard.user_id.id if wizard.user_id else self.env.uid),
            ]
            
            activity = activity.search(domain, order='id desc',limit=1)
            if activity:
                activity.write({
                    'start_time': wizard.start_time,
                    'end_time': wizard.end_time,
                })
                
                record = self.env[wizard.res_model].browse(wizard.res_id)
                record.message_post(body=f"Activity scheduled from {wizard.start_time} to {wizard.end_time}.")
            
            
        return res
    