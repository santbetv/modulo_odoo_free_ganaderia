# -*- coding: utf-8 -*-

from odoo import fields, models


class GanaderiaGanado(models.Model):
    _name = 'ganaderia.ganado' #nombre de mi modelo
    _description = 'Ganado' #describe los datos
    _order = 'nombre_animal asc' #ordenamiento
    fecha_ingreso = fields.Date(string='Fecha de ingreso', required=True)
    nombre_animal = fields.Char(string='Nombre del animal', required=True, size=150, index=True)
    tipo_sexo = fields.Selection(
        [('1', 'Macho'),
         ('2', 'Hembra'),
         ], string='Tipo de Sexo', required=True, index=True, track_visibility='onchange',
        track_sequence=4, default="1")
    raza = fields.Char(string='Raza', required=True, size=150, index=True)
    peso = fields.Char(string='peso', required=True, size=150, index=True)
    edad_meses = fields.Char(string='Edad meses', required=True, size=150, index=True)
    precio = fields.Char(string='Valor de animal', required=True, size=150, index=True)
    estado_corporal = fields.Selection(
        [('1', 'Delgado'),
         ('2', 'Regular'),
         ('3', 'Bueno'),
         ('4', 'Gordo'),
         ], string='Estado corporal', required=True, index=True, track_visibility='onchange',
        track_sequence=5, default="1")
    observacion = fields.Char(string='Observación', required=True, size=150, index=True)
    ciudad_id = fields.Many2one('ganaderia.ciudad', 'Ciudad', required=True)
    #  traigo las ciudades donde yo soy el cobrador de ese modelo
    _sql_constraints = {('ganado_uniq', 'unique(raza)', 'La raza debe ser Única')}

class GanaderiaDepartamento(models.Model):
    _name = 'ganaderia.departamento'  # nombre de mi modelo
    _description = 'Departamento'  # describe los datos
    _order = 'name asc'  # ordenamiento
    name = fields.Char(string='Nombre', required=True, size=150, index=True)
    codigo = fields.Char(string='Codigo', required=True, size=150, index=True)
    _sql_constraints = {('departamento_uniq', 'unique(codigo)', 'El codigo del departamento debe ser Único')}

class GanaderiaCiudad(models.Model):
    _name = 'ganaderia.ciudad'  # nombre de mi modelo
    _description = 'Ciudad'  # describe los datos
    _order = 'name asc'  # ordenamiento
    name = fields.Char(string='Nombre', required=True, size=150, index=True)
    codigo = fields.Char(string='Codigo', required=True, size=150, index=True)
    # Relación una a muchas
    departamento_id =  fields.Many2one('ganaderia.departamento', 'Departamento', required=True)
    _sql_constraints = {('ciudad_uniq', 'unique(codigo)', 'El codigo de la ciudad debe ser Único')}