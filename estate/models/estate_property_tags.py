from odoo import models, fields, api

class EstatePropertyTags(models.Model):
    _name = 'estate.property.tags'
    _description = 'Estate Tags'


    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="color")