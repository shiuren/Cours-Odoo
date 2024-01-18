from odoo import fields, models, api, exceptions
from odoo.fields import Date
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class PlayerGaming(models.Model):
    _name = "player.gaming"
    _inherit = 'mail.thread'
    _description = "Player Gaming"

    name = fields.Char(string="name", tracking=True)
    status = fields.Char(string="Status")
    ranking = fields.Integer(string="Ranking")
    game = fields.Integer(string="Game", compute="_compute_game", store=True)
    win = fields.Integer(string="Win Rate")
    lose = fields.Integer(string="Lose Strike")
    date = fields.Date(string="date of birth")
    patener_ids = fields.Many2many('team.gaming', string="partner", readonly=True)
    equipe = fields.Char(string="equipe", readonly=True)
    offer_ids = fields.One2many('offer.gaming', 'property_id', string='Offre')
    color = fields.Integer(string="color")
    offer_count = fields.Integer(string="Nombre d'offres", compute="_compute_offer_count")
    country = fields.Selection(selection=[
                                            ('europe', 'Europe'),
                                            ('chine', 'Chine'),
                                            ('russie', 'Russie'),
                                            ('usa', 'USA'),
                                            ('afrique', 'Afrique')
                                            ],
                                    
                                )
    genre = fields.Selection(selection=[
                                         ('homme', 'Homme'),
                                         ('femme', 'Femme')       
                                            ],
                                            string="genre"
                                            )
    

    @api.depends('win', 'lose')
    def _compute_game(self):
        for record in self:
            record.game = record.win + record.lose

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    def action_view_offers(self):
        action = self.env.ref('geek_gaming.action_offer_gaming')  # Remplacez 'votre_module' par le nom de votre module
        result = action.read()[0]
        result['domain'] = [('property_id', '=', self.id)]
        return result