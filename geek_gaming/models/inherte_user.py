from odoo import models, fields, api, exceptions

class InheriteUser(models.Model):
    _inherit = 'hr.employee'

    rindra = fields.Char(string="kiki")