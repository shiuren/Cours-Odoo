from odoo import fields, models

class TeamGaming(models.Model):
    _name = "team.gaming"
    _description = "Team Gaming"

    name = fields.Char(string="name")
    team_ids = fields.Many2many('player.gaming', string='team')
