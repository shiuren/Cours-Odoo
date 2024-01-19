# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mtx_project_security(models.Model):
#     _name = 'mtx_project_security.mtx_project_security'
#     _description = 'mtx_project_security.mtx_project_security'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
