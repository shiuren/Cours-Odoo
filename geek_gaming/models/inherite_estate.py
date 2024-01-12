from odoo import models, fields, api, exceptions

class InheriteEstate(models.Model):
    _inherit = 'estate.property.type'

    kiki = fields.Char(string="kiki")