from odoo import models, fields, api

class ResUser(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'vendeur', string='Propriété', domain="[('disponible', '=', True)]")