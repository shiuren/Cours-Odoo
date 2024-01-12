from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError

class CustomeHouse(models.Model):
    _name = 'custome.house'
    _description = 'Custome House'
    _order = 'id DESC'


   
    name = fields.Char(string='Nom', required=True)
    postal_code = fields.Char(string='Code Postal', required=True)    
    categorie_id = fields.Many2one('house.type', string="Type")
    prix = fields.Float(string="Expected Price")
    bestOffer = fields.Float(string="Best Offer")
    selling = fields.Float(string="Selling Price")
    time = fields.Date(string='Aivalable From')
    description = fields.Text(string='déscription')
    bedrooms = fields.Integer(string="bedrooms")
    living_area = fields.Integer(string="living_area")
    facades = fields.Integer(string="facades")
    garage = fields.Boolean(string="garage")
    garden = fields.Boolean(string="garden")
    garden_area = fields.Integer(string="garden_area")
    garden_orientation = fields.Selection([('Notrh', 'Nord'),('South', 'Sud'),('East', 'Est'),('West', 'Ouest')], string='Garden orientation')
    total_area = fields.Float(string="Total Area", compute="_compute_total_area", store=True)

    status = fields.Selection(
        selection=[
            ('draft', "Nouveau"),
            ('received', "Nouveau"),
            ('sell', "Vendue"),
            ('cancel', "Annuler"),
        ],
        string="Status",copy=False,store=True,
        default='draft')

    acheteur = fields.Char(string="acheteur")
    # acheteur_id = fields.Many2one("property.offer", string="Acheteur")
    vendeur_id = fields.Many2one("res.partner", string="Vendeur", default=lambda self: self.env.user.partner_id)
    full_address = fields.Char(string="Adresse Complète", compute="_compute_full_address", store=True)


    nombre_propriete = fields.Integer("Nombre de biens", default=1)
    prix_unitaire = fields.Float(string="Prix unitaire")
    total_price = fields.Float(string="Prix Total", compute="_compute_total_price", store=True)

    #ici je lie offre_ids à celui du champ property_ids qui se trouve dans la table property.offer
    #d'autant plus je fais appelle à ces champs dont j'ai besoin
    offer_ids = fields.One2many("property.offer", "property_id", string="Offres")


    @api.depends('name', 'postal_code')
    def _compute_full_address(self):
        for record in self:
            # Calculer la valeur du champ en combinant le nom, le code postal et le type de maison
            record.full_address = f"{record.name}, {record.postal_code}"

    @api.depends('nombre_propriete', 'prix_unitaire')
    def _compute_total_price(self):
        for record in self:
            
            record.total_price = record.nombre_propriete * record.prix_unitaire

    @api.onchange('nombre_propriete', 'prix_unitaire')
    def _onechange_propriete_price(self):
        for record in self:
                
            self._compute_total_price()

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            
            record.total_area = record.living_area + record.garden_area

    @api.constrains('selling', 'prix')
    def _check_prix_vente_minimum(self):
        for record in self:
            if record.selling > 0:
                if record.selling <  (0.9 * record.prix):
                    raise ValidationError('Le prix de vente ne peut pas être inférieur à 90%\ du prix attendu.')


    # cette action permet de supprimer seul les action non vendue où annuler
    def unlink(self):
        for record in self:
            if record.status not in ['draft', 'cancel']:
                raise UserError("Vous ne pouvez pas supprimer une propriété avec un état différent de 'Nouveau' ou 'Annulé'.")
        return super(CustomeHouse, self).unlink()

    
    #action Annuler et définir une propriété comme vendue.
    def action_cancel(self):
        # Logique pour annuler la propriété  
        if self.status == 'sell':
            raise UserError(_("Ce propriété est déjà vendue")) 
        self.status = 'cancel'   

    def action_sold(self):
        # Logique pour définir la propriété comme vendue
        if self.status == 'cancel':
            raise UserError(_("Ce propriété est déjà annuler")) 
        self.status = 'sell'

    # def action_received(self):
    #     # Logique pour définir la propriété offre reçue
    #     if self.status == 'cancel':
    #         raise UserError(_("Ce propriété est déjà annuler")) 
    #     self.status = 'sell'        

    _sql_constraints = [
        ('check_prix', 'CHECK(prix >= 0)', 'Le prix d\'un bien doit être un nombre positif.'),
    ]
    # house_type_id = fields.Many2one('house.type', 'property_ids')
    house_ids = fields.Many2many('property.offer', widget='statusbar', options="{'statusbar_visible': true}")
    tag_ids = fields.Many2many('house.tag', string="Tags")
    property_id = fields.Many2one('property.offer', string='Propriété')

    #ici create est un methode propre de odoo on n'ajoute rien dans le fichier xml objectif enregistrer un offre et de status accepté
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # status 'nouveau' en 'offre reçue'
            if 'status' in vals:
                if vals['status'] == 'draft':
                    vals['status'] = 'received'
        return super().create(vals_list)

class HouseType(models.Model):
    _name = 'house.type'   
    _description = 'House Type'
    _order = "sequence, name"


    name = fields.Char(string='Name', required=True)
    property_ids = fields.One2many('property.offer', 'house_type_id', string='Property')
    sequence = fields.Integer(string="sequence")
   