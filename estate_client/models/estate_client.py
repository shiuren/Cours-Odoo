

from odoo import models, fields, api,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Ventes'

    client_responsable = fields.Many2one('res.partner',string="Client résponsable")