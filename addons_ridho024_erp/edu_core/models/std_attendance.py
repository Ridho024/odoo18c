from odoo import models,fields

class StdAttendance(models.Model):
    _name = 'std.attendance'
    _description = 'Student Attendance'
    
    student_id = fields.Many2one('res.partner', string='Student', required=True, help='The student for whom the attendance is recorded')
    check_in = fields.Datetime(string='Check In', required=True, help='The date and time when the student checked in')
    check_out = fields.Datetime(string='Check Out', help='The date and time when the student checked out')
    studied_hours = fields.Float(string='Studied Hours', compute='_compute_studied_hours', store=True, help='Total hours studied by the student during the attendance period')