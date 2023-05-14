from odoo import models, fields, api
from datetime import date

class horoscopo(models.Model):
    _inherit = "res.partner"
    fechaNacimiento = fields.Date("Fecha de nacimiento")
    edad = fields.Integer(
        string="Edad", reandonly=True, compute="_calcula_edad", store=True
    )

    signo = fields.Char(
        string="Signo zodiaco", readonly=True, compute="_calcula_signo", store=True
    )

    @api.depends("fechaNacimiento")
    def _calcula_edad(self):
        for registro in self:
            if registro.fechaNacimiento:
                hoy = date.today()
                edad = hoy.year - registro.fechaNacimiento.year - ((hoy.month, hoy.day) < (registro.fechaNacimiento.month, registro.fechaNacimiento.day))
                registro.edad = edad

    @api.depends("fechaNacimiento")
    def _calcula_signo(self):
        try:
            self.ensure_one()
            if self.fechaNacimiento:
                mes = registro.fechaNacimiento.month
                dia = registro.fechaNacimiento.day

                if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
                        self.signo = "Acuario"
                elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
                    self.signo = "Piscis"
                elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
                    self.signo = "Aries"
                elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
                    self.signo = "Tauro"
                elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
                    self.signo = "Géminis"
                elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
                    self.signo = "Cáncer"
                elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
                    self.signo = "Leo"
                elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
                    self.signo = "Virgo"
                elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
                    self.signo = "Libra"
                elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
                    self.signo = "Escorpio"
                elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
                    self.signo = "Sagitario"
                else:
                    self.signo = "Capricornio"
            else:
                self.signo = "Signo TBD"
        except Exception:
            print("Error al calcular el signo zodiacal.")