# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, AccessError


class InheritProjectTask(models.Model):
    _inherit = "project.task"

    # readonly_ah = fields.Boolean(string="Readonly allocated hours")

    # @api.depends('user_ids')
   


    @api.model_create_multi
    def create(self, vals_list):

        res = super(InheritProjectTask, self).create(vals_list)
        x = self.env.user.has_group('mtx_project_security.project_security')
        if not x:
            raise ValidationError("Vous n'avez pas les droits nécessaires pour créer des tâches de projet.")      
        else:
            return res


    is_readonly = fields.Boolean(compute="_compute_readonly_fields", string="test")


    @api.depends('allocated_hours', 'date_deadline')
    def _compute_readonly_fields(self):
        for record in self:
           record.is_readonly = self.env["res.users"].has_group('mtx_project_security.group_readonly')
               
    



