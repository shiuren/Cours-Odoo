from odoo import models, fields, api

class EstateAcheteur(models.Model):
    _name = 'estate.acheteur'
    _description = 'Acheteur'


    name = fields.Char( string="Liste des acheteur", required=True)