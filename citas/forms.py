from django import forms

from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["cliente", "telefono", "servicio", "fecha", "hora", "acepta_datos"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "hora": forms.TimeInput(attrs={"type": "time"}, format="%H:%M"),
        }

    # HU-04: la autorización de datos es obligatoria
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["acepta_datos"].required = True
        self.fields["acepta_datos"].error_messages["required"] = (
            "Debes autorizar el tratamiento de tus datos para agendar la cita."
        )

    # HU-01: no permitir dos citas en la misma fecha y hora
    # HU-02: las citas canceladas ya no ocupan el horario
    def clean(self):
        datos = super().clean()
        fecha = datos.get("fecha")
        hora = datos.get("hora")
        if fecha and hora and Cita.objects.filter(fecha=fecha, hora=hora, estado="activa").exists():
            raise forms.ValidationError("Ya hay una cita agendada en esa fecha y hora. Elige otro horario.")
        return datos
