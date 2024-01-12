from odoo import models, fields

class ResUser(models.Model):
    _inherit = 'res.users'
    _description = 'Res User'

    property_ids = fields.One2many('custome.house', 'vendeur_id', string="Propriété", domaine="[('vendeur_id', '=' ,id)]",)
    # dota = fields.Char(string='Dota')