from odoo import models, fields, api, exceptions
from odoo.fields import Date
from datetime import timedelta, datetime
from odoo.exceptions import ValidationError

class OfferGaming(models.Model):
    _name = 'offer.gaming'
    _description = 'Offer Gaming'

    name = fields.Char(string='Offer')
    salaire = fields.Integer(string='salaire')
    dure = fields.Integer(string='Duré du contrat')
    property_id = fields.Many2one('player.gaming')
    SELECTION_OPTIONS = [('draft', "Nouveau"),
                        ('accepted', "accepté"),
                        ('refused', "Refusé")]
    status = fields.Selection(SELECTION_OPTIONS, string="status", default="draft")

    #ici on a une autre réponse possible les deux conditions mennent aux meme résultat que celui dans dessou
    # def action_accepted(self):
    #     for record in self:
    #         if record.status == 'refused':
    #             raise UserError(_("Cette offre a déjà été refusée. Vous ne pouvez pas l'accepter."))
    #         record.status = 'accepted'
    #         self.property_id.equipe = self.name

    # def action_refused(self):
    #     for record in self:
    #         if record.status == 'accepted':
    #             raise UserError(_("Cette offre a déjà été acceptée. Vous ne pouvez pas la refuser."))
    #         record.status = 'refused'


    def action_accepted(self):
        for record in self:
            if record.status == 'refused':
                # Ancienne approche avec raise
                raise UserError(_("Cette offre a déjà été refusée. Vous ne pouvez pas l'accepter."))
            else:
                record.status = 'accepted'
                self.property_id.equipe = self.name

    def action_refused(self):
        for record in self:
            if record.status == 'accepted':
                # Ancienne approche avec raise
                raise UserError(_("Cette offre a déjà été acceptée. Vous ne pouvez pas la refuser."))
            else:
                record.status = 'refused'    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Vérifier si un enregistrement avec un salaire inférieur existe déjà
            existing_offer = self.search([('salaire', '>', vals.get('salaire', 0.0))], limit=1)
            
            if existing_offer:
                raise ValidationError("Le salaire proposé doit être supérieur ou égal à celui déjà existant.")
        
        return super(OfferGaming, self).create(vals_list)        