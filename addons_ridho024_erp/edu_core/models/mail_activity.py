from odoo import models, fields

class MailActivity(models.Model):
    _inherit = 'mail.activity'

    start_time = fields.Float(string='Start Time', default=8.0, digits=(2, 2))
    end_time = fields.Float(string='End Time', default=17.0, digits=(2, 2))