from .views import RegistroDiarioViewSet  # RegistroDiarioViewSet agregado

from django.urls import path, include
from rest_framework import routers

from .views import ItemViewSet, UserViewSet, PacienteViewSet, MedicoFuncionarioViewSet
from .views import SintomasViewSet  # SintomasViewSet agregado

router = routers.DefaultRouter()
router.register(r'medicofuncionarios', MedicoFuncionarioViewSet, basename='medicofuncionario')
router.register(r'pacientes', PacienteViewSet, basename='paciente')
# router.register(r'items', ItemViewSet, basename='item')
router.register(r'usuarios', UserViewSet, basename='usuario')
router.register(r'sintomas', SintomasViewSet, basename='sintomas')
router.register(r'registros', RegistroDiarioViewSet, basename='registrodiario')

urlpatterns = [
    path('', include(router.urls)),
]