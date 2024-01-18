# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, AccessError


class InheritProjectTask(models.Model):
    _inherit = "project.task"
   

    @api.model_create_multi
    def create(self, vals_list):

        res = super(InheritProjectTask, self).create(vals_list)
        x = self.env.user.has_group('geek_gaming.report_security')
        if not x:
            # import pudb; pudb.set_trace()
            raise ValidationError("Vous n'avez pas les droits nécessaires pour créer des tâches de projet.")      
        else:
            return res


