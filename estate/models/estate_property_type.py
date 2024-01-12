from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Type de Vente'


    name = fields.Char(string="Liste des vendeur", required=True)