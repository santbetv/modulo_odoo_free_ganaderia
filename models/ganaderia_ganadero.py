# -*- coding: utf-8 -*-

from odoo import fields, models


class GanaderiaGandero(models.Model):
    _name = 'ganaderia.ganadero' #nombre de mi modelo
    _description = 'Ganadero' #describe los datos
    _order = 'nombre asc' #ordenamiento
    # Relacion estatica
    # Indicamos seguimiento a la visibilidad con metodo onchange
    # Orden la accion con track_sequence
    # valor con por defecto en caja default
    tipo_documento = fields.Selection(
        [('1', 'Cédula de ciudadania'),
         ('2', 'NIT'),
         ('3', 'Cédula de extranjeria'),
         ('4', 'Pasaporte'),
         ], string='Tipo de Documento', required=True, index=True, track_visibility='onchange',
        track_sequence=1, default="1")
    documento = fields.Char(string='Numero de documento', required=True, size=150, index=True)
    nombre = fields.Char(string='Nombre', required=True, size=150, index=True)
    apellido = fields.Char(string='Apellido', required=True, size=150, index=True)
    movil = fields.Char(string='Movil', required=True, size=150, index=True)
    email = fields.Char(string='Email', required=True, size=150, index=True)
    fecha_nacimiento = fields.Date(string='Fecha nacimiento', required=True)
    ano_negocio = fields.Selection(
        [('1', 'De 1 a 2'),
         ('2', 'De 3 a 5'),
         ('3', 'Más de 5'),
         ], string='Años en el negocio', required=True, index=True, track_visibility='onchange',
        track_sequence=8, default="1")
    _sql_constraints = {('ganadero_uniq', 'unique(documento)', 'El numero de documento debe ser Único')}