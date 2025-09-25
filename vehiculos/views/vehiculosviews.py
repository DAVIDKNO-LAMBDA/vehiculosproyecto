from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import date, timedelta

from ..models import Vehiculo
from ..serializers import VehiculoSerializer, VehiculoDisponibleSerializer, VehiculoAlertaSerializer


# Listar todos los vehículos
class VehiculoListView(APIView):
    def get(self, request):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

# Listar vehículos disponibles
class VehiculoDisponibleListView(APIView):
    def get(self, request):
        vehiculos = Vehiculo.objects.filter(disponible=True)
        serializer = VehiculoDisponibleSerializer(vehiculos, many=True)
        return Response(serializer.data)

# Alertas de vencimiento
class VehiculoAlertaListView(APIView):
    def get(self, request):
        hoy = date.today()
        vehiculos = []
        for v in Vehiculo.objects.all():
            if v.fecha_vencimiento_soat <= hoy + timedelta(days=30) or v.fecha_vencimiento_tecno <= hoy + timedelta(days=30):
                vehiculos.append(v)
        serializer = VehiculoAlertaSerializer(vehiculos, many=True)
        return Response(serializer.data)

# Crear vehículo
class VehiculoCrearView(APIView):
    def post(self, request):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Actualizar vehículo
class VehiculoActualizarView(APIView):
    def put(self, request, vehiculo_id):
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        serializer = VehiculoSerializer(vehiculo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Actualizar disponibilidad
class VehiculoActualizarDisponibilidadView(APIView):
    def post(self, request, vehiculo_id):
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        disponible = request.data.get('disponible')
        if disponible is None:
            return Response({"error": "Debes enviar 'disponible': true o false"}, status=status.HTTP_400_BAD_REQUEST)
        vehiculo.disponible = disponible
        vehiculo.save()
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)

# Eliminar vehículo
class VehiculoEliminarView(APIView):
    def delete(self, request, vehiculo_id):
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        vehiculo.delete()
        return Response({"mensaje": f"Vehículo {vehiculo.placa} eliminado"}, status=status.HTTP_204_NO_CONTENT)
