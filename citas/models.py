from django.db import models


class Cita(models.Model):
    SERVICIOS = [
        ("consulta", "Consulta médica"),
        ("peluqueria", "Peluquería"),
        ("veterinaria", "Veterinaria"),
        ("estetica", "Centro estético"),
    ]
    # HU-02: estado de la cita
    ESTADOS = [
        ("activa", "Activa"),
        ("cancelada", "Cancelada"),
    ]

    cliente = models.CharField("Nombre del cliente", max_length=100)
    telefono = models.CharField("Teléfono", max_length=20)
    servicio = models.CharField("Servicio", max_length=20, choices=SERVICIOS)
    fecha = models.DateField("Fecha")
    hora = models.TimeField("Hora")
    estado = models.CharField("Estado", max_length=10, choices=ESTADOS, default="activa")
    # HU-04: autorización de tratamiento de datos (Ley 1581 de 2012)
    acepta_datos = models.BooleanField(
        "Autorizo el tratamiento de mis datos personales (Ley 1581 de 2012)",
        default=False,
    )
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha", "hora"]

    def __str__(self):
        return f"{self.cliente} - {self.fecha} {self.hora}"
