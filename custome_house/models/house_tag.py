from odoo import models, fields, api,_

class HouseTag(models.Model):
    _name = 'house.tag'
    _description = 'House Tag'
    

    name = fields.Char(string="Name", required=True)
    color = fields.Char(string="Color")