from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class Incidencias(models.Model):
    Estado = models.CharField(max_length=30)
    Sede = models.CharField(max_length=30)
    Departamento = models.CharField(max_length=30)
    Tipoincidencia = models.CharField(max_length=30)
    Usuario = models.CharField(max_length=30)
    Observaciones = models.CharField(max_length=100)
