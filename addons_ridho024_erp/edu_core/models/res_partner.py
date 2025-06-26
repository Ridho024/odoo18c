from odoo import models,fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_student = fields.Boolean(string='Is Student', help='Indicates if the partner is a student (EMS)')
    nisn = fields.Char(string='NISN', help='Official identification number for students (National Student Identification Number)')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    student_status = fields.Selection([('inactive', 'Inactive'),
                                       ('active', 'Active'),
                                       ('graduated', 'Graduated'),
                                       ('drop_out', 'Dropped Out')],
                                      string='Enrollment Status', default='inactive', help='Current enrollment status of the student')
    
