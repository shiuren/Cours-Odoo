# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.fields import Date
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Propriété Immobiliaire'


    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="postcode")
    date_availability = fields.Date(string="Aivalable from", default=lambda self: fields.Date.today() + timedelta(days=90))
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('North', 'Nord'),('South', 'Sud'),('East', 'Est'),('West', 'Ouest')], string='Type')
    vendeur = fields.Char(string="Vendeur")
    acheteur = fields.Char(string="Acheteur")
    tags_ids = fields.Many2many('estate.property.tags', string='Tags')
    # offre_ids ici permet de faire applle au vue formulaire de estate property offer
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Property Offers')
    total_area = fields.Float(string="Total Area", compute="_compute_total_area", store=True)
    best_price = fields.Float(string='Best offer', compute='_compute_best_price', store=True)
    status = fields.Selection(
        selection=[
            ('draft', "New"),
            ('received', "Offer received"),
            ('sell', "Sell"),
            ('cancel', "Cancel"), 
        ],
        string="Status",copy=False,store=True,
        default='draft')

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'Le prix du bien doit être positif.'),
    ]

    _sql_constraints = [
        ('check_best_price', 'CHECK(best_price >= 0)', 'Le prix de l\'offre doit être positif.'),
    ]


    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            
            record.total_area = record.living_area + record.garden_area


    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            best_price = max(record.offer_ids.mapped('price'), default=0.0)
            record.best_price = best_price


    @api.onchange('garden')
    def _onchange_garden(self):
        if not self.garden:
            # Si le jardin n'est pas défini, effacer les valeurs
            self.garden_area = 0
            self.garden_orientation = False
        else:
            # Si le jardin est défini, définir des valeurs par défaut
            self.garden_area = 10
            self.garden_orientation = 'North'

        # cette action permet de supprimer seul les action non vendue où annuler
    def unlink(self):
        for record in self:
            if record.status not in ['draft', 'cancel']:
                raise UserError("Vous ne pouvez pas supprimer une propriété avec un état différent de 'Nouveau' ou 'Annulé'.")
        return super(EstateProperty, self).unlink()
   

    def action_cancel(self):
        for record in self:
            if record.status == 'sell':
                raise UserError(_("Cette propriété est déjà vendue. Vous ne pouvez pas l'annuler."))
            record.status = 'cancel'

    
    def action_sold(self):
        for record in self:
            if record.status == 'cancel':
                raise UserError(_("Cette propriété est annulée. Vous ne pouvez pas la vendre."))
            record.status = 'sell'

    #ici create est un methode propre de odoo on n'ajoute rien dans le fichier xml objectif enregistrer un offre et de status accepté
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # status 'nouveau' en 'offre reçue'
            if 'status' in vals:
                if vals['status'] == 'draft':
                    vals['status'] = 'received'
        return super().create(vals_list)