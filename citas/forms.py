from django import forms

from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["cliente", "telefono", "servicio", "fecha", "hora"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "hora": forms.TimeInput(attrs={"type": "time"}, format="%H:%M"),
        }

    # HU-01: no permitir dos citas en la misma fecha y hora
    def clean(self):
        datos = super().clean()
        fecha = datos.get("fecha")
        hora = datos.get("hora")
        if fecha and hora and Cita.objects.filter(fecha=fecha, hora=hora).exists():
            raise forms.ValidationError("Ya hay una cita agendada en esa fecha y hora. Elige otro horario.")
        return datos
