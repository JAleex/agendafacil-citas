from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_citas, name="lista_citas"),
    path("nueva/", views.nueva_cita, name="nueva_cita"),
    path("<int:cita_id>/cancelar/", views.cancelar_cita, name="cancelar_cita"),
]
