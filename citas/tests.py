# HU-05: pruebas automáticas de las reglas de las citas
# Se ejecutan con: python manage.py test
from datetime import date, time

from django.test import TestCase
from django.urls import reverse

from .forms import CitaForm
from .models import Cita


class CitaTests(TestCase):
    def datos_formulario(self, **cambios):
        datos = {
            "cliente": "Ana Pérez",
            "telefono": "3001234567",
            "servicio": "peluqueria",
            "fecha": "2026-12-01",
            "hora": "10:00",
            "acepta_datos": True,
        }
        datos.update(cambios)
        return datos

    def crear_cita(self, **cambios):
        datos = {
            "cliente": "Luis Gómez",
            "telefono": "3009998877",
            "servicio": "consulta",
            "fecha": date(2026, 12, 1),
            "hora": time(10, 0),
        }
        datos.update(cambios)
        return Cita.objects.create(**datos)

    def test_crear_cita_valida(self):
        respuesta = self.client.post(reverse("nueva_cita"), self.datos_formulario())
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Cita.objects.count(), 1)

    def test_no_permite_cruce_de_horario(self):
        self.crear_cita()
        form = CitaForm(data=self.datos_formulario())
        self.assertFalse(form.is_valid())

    def test_cita_cancelada_libera_el_horario(self):
        self.crear_cita(estado="cancelada")
        form = CitaForm(data=self.datos_formulario())
        self.assertTrue(form.is_valid())

    def test_cancelar_cita(self):
        cita = self.crear_cita()
        self.client.post(reverse("cancelar_cita", args=[cita.id]))
        cita.refresh_from_db()
        self.assertEqual(cita.estado, "cancelada")

    def test_filtrar_por_fecha(self):
        self.crear_cita(fecha=date(2026, 12, 1))
        self.crear_cita(fecha=date(2026, 12, 2))
        respuesta = self.client.get(reverse("lista_citas"), {"fecha": "2026-12-01"})
        self.assertEqual(len(respuesta.context["citas"]), 1)

    def test_debe_autorizar_tratamiento_de_datos(self):
        form = CitaForm(data=self.datos_formulario(acepta_datos=False))
        self.assertFalse(form.is_valid())
