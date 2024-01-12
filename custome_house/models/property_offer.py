from odoo import models, fields, api
from odoo.fields import Date
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = "property.offer"
    _description = "Property Offer"
    _order = "prix DESC"


    SELECTION_OPTIONS = [('draft', "Nouveau"),
                         ('accepted', "accepté"),
                         ('cancel', "Annuler")]

    nb_jour = fields.Integer(string='nombre de jour')
    date_deadline = fields.Date(compute='_compute_date_deadline', string='Date limite')
    date_actuel = fields.Date(string="Date de publication")
    property_id = fields.Many2one('custome.house',string="House")
    name = fields.Char(string="Acheteur", required=True)
    status = fields.Selection(SELECTION_OPTIONS, default='draft', string="offre")
    prix = fields.Float(string="prix de l'offre")
    house_type_id = fields.Many2one('house.type', 'property_ids')
    

    @api.depends('nb_jour', 'date_actuel')
    def _compute_date_deadline(self):
        for record in self:
            if record.date_actuel and record.nb_jour:
                record.date_deadline = record.date_actuel + timedelta(days=record.nb_jour)
            else:
                record.date_deadline = False

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_actuel and record.date_deadline:
                record.nb_jour = (record.date_deadline - record.date_actuel).days
            else:
                record.nb_jour = 0

    _sql_constraints = [
        ('check_prix', 'CHECK(prix >= 0)', 'Le prix d\'une offre doit être un nombre positif.'),
    ]
    
    #action Annuler et définir une propriété comme vendue.
    def action_cancel(self):
        self.status = 'cancel'   

    #je fait appelle à selling par le chemin property_id qui est un Many2one pour le synchronisé à la valeur de prix
    def action_sold(self):
        self.status = 'accepted'
        self.property_id.selling = self.prix
        self.property_id.acheteur = self.name

   
    