from datetime import date

from django.shortcuts import get_object_or_404, redirect, render

from .forms import CitaForm
from .models import Cita


def lista_citas(request):
    citas = Cita.objects.all()

    # HU-03: filtrar por fecha (?fecha=AAAA-MM-DD)
    fecha = request.GET.get("fecha", "")
    if fecha:
        try:
            citas = citas.filter(fecha=date.fromisoformat(fecha))
        except ValueError:
            fecha = ""

    return render(request, "citas/lista.html", {"citas": citas, "fecha": fecha})


def nueva_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_citas")
    else:
        form = CitaForm()
    return render(request, "citas/formulario.html", {"form": form})


# HU-02: cancelar una cita
def cancelar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == "POST":
        cita.estado = "cancelada"
        cita.save()
    return redirect("lista_citas")
