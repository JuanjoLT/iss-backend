from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Paciente(models.Model):
    usuario_id = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_diagnostico = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Paciente {self.usuario_id}"

class MedicoFuncionario(models.Model):
    usuario_id = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    unidad_referencia_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"MedicoFuncionario {self.usuario_id}"
    
class Sintomas(models.Model):
    nombre = models.CharField(max_length=100)
    puntacion = models.IntegerField(default=0)

class RegistroDiario(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    puntaje_total = models.IntegerField(default=0)
    estado = models.CharField(max_length=50, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ], default='activo')
    