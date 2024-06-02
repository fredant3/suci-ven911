from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

#BASE DE DATOS DEL MODULO PLANIFICACION
class Objetivos(models.Model):
    fechai = models.DateField(verbose_name='Fecha de Inicio')
    fechaf = models.DateField(verbose_name='Fecha Final')
    objetiv = models.CharField(max_length=64, verbose_name='Objetivos:', default='')
    meta = models.CharField(max_length=64, verbose_name='Meta:', default='')

#BASE DE DATOS DEL MODULO ACTIVIDADES
class Actividades(models.Model):
    fechai = models.DateField(verbose_name='Fecha de Inicio')
    fechaf = models.DateField(verbose_name='Fecha Final')
    objetiv = models.CharField(max_length=64, verbose_name='Objetivos:', default='')
    meta = models.CharField(max_length=64, verbose_name='Meta:', default='')
