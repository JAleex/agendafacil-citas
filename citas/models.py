from django.db import models


class Cita(models.Model):
    SERVICIOS = [
        ("consulta", "Consulta médica"),
        ("peluqueria", "Peluquería"),
        ("veterinaria", "Veterinaria"),
        ("estetica", "Centro estético"),
    ]

    cliente = models.CharField("Nombre del cliente", max_length=100)
    telefono = models.CharField("Teléfono", max_length=20)
    servicio = models.CharField("Servicio", max_length=20, choices=SERVICIOS)
    fecha = models.DateField("Fecha")
    hora = models.TimeField("Hora")
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha", "hora"]

    def __str__(self):
        return f"{self.cliente} - {self.fecha} {self.hora}"
