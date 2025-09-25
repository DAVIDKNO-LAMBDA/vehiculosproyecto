# vehiculos/urls.py
from django.urls import path
from .views import (
    VehiculoListView,
    VehiculoDisponibleListView,
    VehiculoAlertaListView,
    VehiculoCrearView,
    VehiculoActualizarView,
    VehiculoActualizarDisponibilidadView,
    VehiculoEliminarView,
)

urlpatterns = [
    # Listados
    path("list/", VehiculoListView.as_view(), name="vehiculo-list"),
    path("disponibles/", VehiculoDisponibleListView.as_view(), name="vehiculo-disponibles"),
    path("alertas/", VehiculoAlertaListView.as_view(), name="vehiculo-alertas"),

    # CRUD
    path("crear/", VehiculoCrearView.as_view(), name="vehiculo-crear"),
    path("actualizar/<int:vehiculo_id>/", VehiculoActualizarView.as_view(), name="vehiculo-actualizar"),
    path("actualizar-disponibilidad/<int:vehiculo_id>/", VehiculoActualizarDisponibilidadView.as_view(), name="vehiculo-actualizar-disponibilidad"),
    path("eliminar/<int:vehiculo_id>/", VehiculoEliminarView.as_view(), name="vehiculo-eliminar"),
]
