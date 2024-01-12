# -*- coding: utf-8 -*-
# from odoo import http


# class CustomeHouse(http.Controller):
#     @http.route('/custome_house/custome_house', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custome_house/custome_house/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome_house.listing', {
#             'root': '/custome_house/custome_house',
#             'objects': http.request.env['custome_house.custome_house'].search([]),
#         })

#     @http.route('/custome_house/custome_house/objects/<model("custome_house.custome_house"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custome_house.object', {
#             'object': obj
#         })
