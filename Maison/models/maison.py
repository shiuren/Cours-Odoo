from odoo import fields, models

class Maison(models.Model):
    _name = 'maison.maison'


    name = fields.Char(string='Anarana')
    mpivarotra = fields.Many2one('pivarotra.maison', string='Mpivarotra')
    vidiny = fields.Float(string='Vidiny')
    daty = fields.Date(string='Daty famarotana')