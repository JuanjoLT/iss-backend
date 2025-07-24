from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .models import RegistroDiario
from .serializers import RegistroDiarioSerializer
class RegistroDiarioViewSet(viewsets.ModelViewSet):
    """
    CRUD de registro diario:
      - GET    /api/registrodiario/       → lista registros
      - POST   /api/registrodiario/       → crea registro
      - GET    /api/registrodiario/{id}/  → detalle
      - PUT    /api/registrodiario/{id}/  → actualiza
      - PATCH  /api/registrodiario/{id}/  → parches
      - DELETE /api/registrodiario/{id}/  → elimina
    """
    queryset = RegistroDiario.objects.all()
    serializer_class = RegistroDiarioSerializer

from .models import Item, Paciente, MedicoFuncionario  
from .serializers import ItemSerializer, UserSerializer, PacienteSerializer, MedicoFuncionarioSerializer  # ItemSerializer comentado en uso abajo
from .models import Sintomas
from .serializers import SintomasSerializer
class MedicoFuncionarioViewSet(viewsets.ModelViewSet):
    """
    CRUD de médicos funcionarios:
      - GET    /api/medicofuncionarios/       → lista
      - POST   /api/medicofuncionarios/       → crea
      - GET    /api/medicofuncionarios/{id}/  → detalle
      - PUT    /api/medicofuncionarios/{id}/  → actualiza
      - PATCH  /api/medicofuncionarios/{id}/  → parches
      - DELETE /api/medicofuncionarios/{id}/  → elimina
    """
    queryset = MedicoFuncionario.objects.all()
    serializer_class = MedicoFuncionarioSerializer
class SintomasViewSet(viewsets.ModelViewSet):
    """
    CRUD de síntomas:
      - GET    /api/sintomas/       → lista síntomas
      - POST   /api/sintomas/       → crea síntoma
      - GET    /api/sintomas/{id}/  → detalle
      - PUT    /api/sintomas/{id}/  → actualiza
      - PATCH  /api/sintomas/{id}/  → parches
      - DELETE /api/sintomas/{id}/  → elimina
    """
    queryset = Sintomas.objects.all()
    serializer_class = SintomasSerializer
class PacienteViewSet(viewsets.ModelViewSet):
    """
    CRUD de pacientes:
      - GET    /api/pacientes/       → lista pacientes
      - POST   /api/pacientes/       → crea paciente
      - GET    /api/pacientes/{id}/  → detalle
      - PUT    /api/pacientes/{id}/  → actualiza
      - PATCH  /api/pacientes/{id}/  → parches
      - DELETE /api/pacientes/{id}/  → elimina
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

User = get_user_model()

class ItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD de Item:
    - GET     /api/items/        → lista items
    - POST    /api/items/        → crea un nuevo item
    - GET     /api/items/{pk}/   → detalle
    - PUT     /api/items/{pk}/   → actualiza
    - DELETE  /api/items/{pk}/   → elimina
    """
    # Queryset base: todos los Items
    queryset = Item.objects.all()
    # Serializer que convierte Item <→ JSON
    serializer_class = ItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD de usuarios:
      - GET    /api/users/       → lista usuarios
      - POST   /api/users/       → crea usuario
      - GET    /api/users/{id}/  → detalle
      - PUT    /api/users/{id}/  → actualiza
      - PATCH  /api/users/{id}/  → parches
      - DELETE /api/users/{id}/  → elimina
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
