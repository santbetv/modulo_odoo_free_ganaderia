# -*- coding: utf-8 -*-

from odoo import fields, models


class GanaderiaFinca(models.Model):
    _name = 'ganaderia.finca' #nombre de mi modelo
    _description = 'Finca' #describe los datos
    _order = 'nombre_finca asc' #ordenamiento
    nombre_finca = fields.Char(string='Nombre de la finca', required=True, size=150, index=True)
    altitud = fields.Char(string='Altitud', required=True, size=150, index=True)
    area_ganaderia = fields.Char(string='Area de ganaderia', required=True, size=150, index=True)
    tipo_area = fields.Selection(
        [('1', 'Cuadras'),
         ('2', 'Hectarias'),
         ], string='Tipo de area', required=True, index=True, track_visibility='onchange',
        track_sequence=4, default="1")
    description = fields.Char(string='Descripcion', required=True, size=150, index=True)
    ganadero_id = fields.Many2one('ganaderia.ganadero', 'Ganadero', required=True)
    ganado_id = fields.Many2one('ganaderia.ganado', 'Ganado', required=True)