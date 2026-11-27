from django.shortcuts import get_object_or_404, redirect, render

from .forms import CitaForm
from .models import Cita


def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, "citas/lista.html", {"citas": citas})


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
