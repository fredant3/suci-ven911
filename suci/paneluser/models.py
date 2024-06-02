from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class Usuarios(AbstractUser, PermissionsMixin):

    STATUS = (
        ('estandar', 'estandar'),
        ('admin', 'admin'),
        ('superu', 'superu'),
    )

    username = models.CharField(max_length=200, verbose_name='Cédula:', default='', unique=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=200, verbose_name='Apellido:', default='')
    password = models.CharField(max_length=200, verbose_name='Contraseña:', default='')
    tipo = models.CharField(max_length=200, verbose_name='Tipo de Usuario:', choices=STATUS, default='')
    sede = models.CharField(max_length=200, verbose_name='Sede:', default='')
    departamento = models.CharField(max_length=200, verbose_name='Departamento:', default='')
    estado = models.CharField(max_length=200, verbose_name='Estado:', default='')
    correo = models.EmailField(max_length=200, verbose_name='Correo:', default='')
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
class Departamentos(models.Model):
    departamento = models.CharField(max_length=64, verbose_name='Departamento:', default='', unique=True)
    estado = models.CharField(max_length=64, verbose_name='Estado:', default='', unique=True)


class Sedes(models.Model):
    direccion = models.CharField(max_length=64, verbose_name='Direccion:', default='', unique=True)
    municipio = models.CharField(max_length=64, verbose_name='Municipio:', default='', unique=True)
    estado = models.CharField(max_length=64, verbose_name='Estado:', default='', unique=True)