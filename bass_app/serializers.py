from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Item, Paciente, MedicoFuncionario, Sintomas, RegistroDiario
class RegistroDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDiario
        fields = ['id', 'paciente_id', 'fecha', 'puntaje_total', 'estado']
class SintomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintomas
        fields = ['id', 'nombre', 'puntacion']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'usuario_id', 'direccion', 'telefono', 'fecha_nacimiento', 'fecha_diagnostico']
        read_only_fields = ['id']

class MedicoFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoFuncionario
        fields = ['id', 'usuario_id', 'profesion', 'telefono', 'direccion', 'unidad_referencia_id']
        read_only_fields = ['id']

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
        read_only_fields = ['id', 'is_active']
        extra_kwargs = {
            'email': {'required': True},
        }




