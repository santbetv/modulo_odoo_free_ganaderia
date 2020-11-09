# -*- coding: utf-8 -*-
from lxml.html.diff import token
from odoo import fields, models, api
import requests
import json
import logging
from pyatspi import state

from odoo.addons.restful.common import default

_logger = logging.getLogger(__name__)

class GanaderiaGanado(models.Model):
    _name = 'ganaderia.ganado' #nombre de mi modelo
    _description = 'Ganado' #describe los datos
    _order = 'nombre_animal asc' #ordenamiento
    _rec_name = 'nombre_animal'
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
    state = fields.Selection(
        [('enestudio', 'En estudio'),
         ('approved', 'Aprobado'),
         ('refused', 'Rechazado'),
         ], string='Estado', required=True, track_visibility='onchange',
        track_sequence=11, default="enestudio")
    respuesta_rasp = fields.Char(string='Aceptando ganado', required=True, size=150, default="Sin respuesta")
    accion_rasp = fields.Char(string='Apertura de puerta', required=True, size=150, default="Sin respuesta")
    ciudad_id = fields.Many2one('ganaderia.ciudad', 'Ciudad', required=True)
    #  traigo las ciudades donde yo soy el cobrador de ese modelo
    _sql_constraints = {('ganado_uniq', 'unique(raza)', 'La raza debe ser Única')}

    def aprobar_ganado(self):

        url = "https://eloquent-salamander-3759.dataplicity.io/auth"
        urlEncender = "https://eloquent-salamander-3759.dataplicity.io/led/red/"

        payload = "{\n    \"username\": \"carloaiza@umanizales.edu.co\",\n    \"password\": \"prueba\"\n}"
        payloadEncender = "{\n    \"state\":\"1\"\n}"

        headers = {
          'Content-Type': 'application/json'
        }


        response = requests.post(url, data = payload, headers=headers)

        if response.status_code >= 200 and response.status_code <= 300:

            token = response.json()['access_token']

            headers['Authorization'] = "{0} {1}".format("JWT", token)

            respuestaEncendido = requests.post(urlEncender, data = payloadEncender, headers=headers)

            if respuestaEncendido.status_code >= 200 and respuestaEncendido.status_code <= 300:

                #print(respuestaEncendido.text.encode('utf8'))
                #self.write({'respuesta_rasp':str(respuestaEncendido.content).replace("b", "")})
                estadoRespuesta = respuestaEncendido.json()['red']
                if estadoRespuesta == "1":
                    self.write({'respuesta_rasp': 'Activado en Raspberry'})
                    self.write({'state': 'approved'})
            else:
                _logger.info("Se tiene error en paso encendido" )
        else:
            _logger.info("Se tiene error en validar token")

    def rechazar_ganado(self):

        url = "https://eloquent-salamander-3759.dataplicity.io/auth"
        urlEncender = "https://eloquent-salamander-3759.dataplicity.io/led/red/"

        payload = "{\n    \"username\": \"carloaiza@umanizales.edu.co\",\n    \"password\": \"prueba\"\n}"
        payloadEncender = "{\n    \"state\":\"0\"\n}"

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, data=payload, headers=headers)

        if response.status_code >= 200 and response.status_code <= 300:

            token = response.json()['access_token']

            headers['Authorization'] = "{0} {1}".format("JWT", token)

            respuestaEncendido = requests.post(urlEncender, data=payloadEncender, headers=headers)

            if respuestaEncendido.status_code >= 200 and respuestaEncendido.status_code <= 300:

                print(respuestaEncendido.text.encode('utf8'))

                # self.write({'state': 'approved'})
                #self.write({'respuesta_rasp': str(respuestaEncendido.text.encode('utf8'))})
                estadoRespuesta = respuestaEncendido.json()['red']
                if estadoRespuesta == "0":
                    self.write({'respuesta_rasp': 'Inactivo en Raspberry'})
                    self.write({'state': 'refused'})
            else:
                _logger.info("Se tiene error en paso encendido" )
        else:
            _logger.info("Se tiene error en validar token")


    def devolver_ganado(self):
        self.write({'state': 'enestudio'})


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