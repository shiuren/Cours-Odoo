from odoo import models, fields, api, exceptions
from odoo.fields import Date
from datetime import timedelta, datetime

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Offer'


    price = fields.Float(string="Price")

    SELECTION_OPTIONS = [('draft', "Nouveau"),
                        ('accepted', "accepté"),
                        ('refused', "Refusé")]

    status = fields.Selection(SELECTION_OPTIONS, default='draft', string="status")
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property')
    validity = fields.Integer(string='validity Days', default=7)
    date_deadline = fields.Date(string='deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline', store=True)




    @api.depends('validity', 'date_deadline')
    def _compute_date_deadline(self):
        for record in self:
            if record.date_deadline and record.validity:
                record.date_deadline = record.date_deadline + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.validity:
                record.validity = (record.date_deadline - datetime.now().date()).days
            else:
                record.validity = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:

            # Vérification du montant inférieur à une offre existante
            if 'price' in vals and 'property_id' in vals:
                property_obj = self.env['estate.property'].browse(vals['property_id'])
                existing_offer = self.search([
                    ('property_id', '=', vals['property_id']),
                    ('status', '=', 'accepted'),
                    ('price', '>', vals['price']),
                ], limit=1)

                if existing_offer:
                    raise exceptions.UserError("Vous ne pouvez pas créer une offre avec un montant inférieur à une offre exist")

        return super().create(vals_list)
        
        
    #condition si l'offre a été accepté afficher le prix de vente ainsi que le nom de lacheteur
    def action_accepted(self):
        for record in self:
            if record.status == 'refused':
                raise UserError(_("Cette offre a déjà été refusée. Vous ne pouvez pas l'accepter."))
            record.status = 'accepted'
            self.property_id.selling_price = self.price
            self.property_id.acheteur = self.partner_id    
                

        
    def action_refused(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError(_("Cette offre a déjà été acceptée. Vous ne pouvez pas la refuser."))
            record.status = 'refused'

