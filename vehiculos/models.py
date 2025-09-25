from django.db import models

from django.db import models
from django.utils import timezone
from datetime import timedelta


class Vehiculo(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('alquilado', 'Alquilado'),
        ('mantenimiento', 'Mantenimiento'),
        ('inactivo', 'Inactivo'),
    ]

    placa = models.CharField(max_length=10, unique=True)  # identificador único
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    color = models.CharField(max_length=30, blank=True, null=True)
    kilometraje = models.PositiveIntegerField(default=0)

    # Documentos
    soat_vencimiento = models.DateField()
    tecnomecanica_vencimiento = models.DateField()

    # Estado y disponibilidad
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    disponible = models.BooleanField(default=True)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"

    @property
    def soat_vencido(self):
        return self.soat_vencimiento < timezone.now().date()

    @property
    def tecnomecanica_vencida(self):
        return self.tecnomecanica_vencimiento < timezone.now().date()

    @property
    def proximo_vencimiento(self):
        """Devuelve cuál documento vence primero"""
        fechas = {
            'SOAT': self.soat_vencimiento,
            'Tecnomecánica': self.tecnomecanica_vencimiento,
        }
        return min(fechas, key=fechas.get)


# Create your models here.
