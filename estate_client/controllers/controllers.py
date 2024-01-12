# -*- coding: utf-8 -*-
# from odoo import http


# class EstateClient(http.Controller):
#     @http.route('/estate_client/estate_client', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate_client/estate_client/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate_client.listing', {
#             'root': '/estate_client/estate_client',
#             'objects': http.request.env['estate_client.estate_client'].search([]),
#         })

#     @http.route('/estate_client/estate_client/objects/<model("estate_client.estate_client"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate_client.object', {
#             'object': obj
#         })
