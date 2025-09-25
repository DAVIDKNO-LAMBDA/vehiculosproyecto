from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/vehiculos/", include("vehiculos.urls")),  # aquí se conectan las rutas de vehiculos
]
