from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

#BASE DE DATOS DEL MODULO PRESUPUESTO - PROYECTO
class Proyecto(models.Model):
    id = models.CharField(max_length=64, verbose_name='ID:', default=''),
    nombrep = models.CharField(max_length=64, verbose_name='Nombre del Proyecto:', default='')
    fechai = models.DateField(verbose_name='Fecha de Inicio')
    fechac = models.DateField(verbose_name='Fecha de Culminación')
    situacionp = models.CharField(max_length=64, verbose_name='Situación Presupuestaria:', default='')
    montoproyecto = models.CharField(max_length=64, verbose_name='Monto Total del Proyecto:', default='')
    responsableg = models.CharField(max_length=64, verbose_name='Responsable Gerente:', default='')
    responsablet = models.CharField(max_length=64, verbose_name='Responsable Técnico:', default='')
    responsabler = models.CharField(max_length=64, verbose_name='Responsable Registrador:', default='')
    responsablea = models.CharField(max_length=64, verbose_name='Responsable Administrativo:', default='')
    estatus = models.CharField(max_length=64, verbose_name='Estatus del Proyecto:', default='')

#BASE DE DATOS DEL MODULO PRESUPUESTO - ACCIONES CENTRALIZADAS
class Acciones(models.Model):
    id = models.CharField(max_length=64, verbose_name='ID:', default=''),
    nombrep = models.CharField(max_length=64, verbose_name='Nombre del Proyecto:', default='')
    fechai = models.DateField(verbose_name='Fecha de Inicio')
    fechac = models.DateField(verbose_name='Fecha de Culminación')
    situacionp = models.CharField(max_length=64, verbose_name='Situación Presupuestaria:', default='')
    montoproyecto = models.CharField(max_length=64, verbose_name='Monto Total del Proyecto:', default='')
    responsableg = models.CharField(max_length=64, verbose_name='Responsable Gerente:', default='')
    responsablet = models.CharField(max_length=64, verbose_name='Responsable Técnico:', default='')
    responsabler = models.CharField(max_length=64, verbose_name='Responsable Registrador:', default='')
    responsablea = models.CharField(max_length=64, verbose_name='Responsable Administrativo:', default='')
    estatus = models.CharField(max_length=64, verbose_name='Estatus del Proyecto:', default='')

#BASE DE DATOS DEL MODULO PRESUPUESTO - ASIGNACION
class Asignacion(models.Model):
    id = models.CharField(max_length=64, verbose_name='ID:', default=''),
    nombredir= models.CharField(max_length=64, verbose_name='Nombre de la dirección:', default='')
    presuasig = models.CharField(max_length=64, verbose_name='Presupuesto asignado:', default='')
    objeanual = models.CharField(max_length=64, verbose_name='Objetivo general anual:', default='')
    numpartida = models.CharField(max_length=10, verbose_name='Número de partida:', default='')
     
#BASE DE DATOS DEL MODULO PRESUPUESTO - CEDENTE
class Cedente(models.Model):
    idc = models.CharField(max_length=100, verbose_name='Id Cedente:', default='')
    partidac = models.CharField(max_length=64, verbose_name='Partida', default='')
    generalc = models.CharField(max_length=64, verbose_name='General', default='')
    espefc = models.CharField(max_length=64, verbose_name='Específicaciones', default='')
    subespefc = models.CharField(max_length=64, verbose_name='Sub-Especialidad', default='')
    denomc = models.CharField(max_length=64, verbose_name='Denomincación', default='')
    presuacorc = models.CharField(max_length=64, verbose_name='Presupuesto acordado', default='')
    caufechac = models.CharField(max_length=64, verbose_name='Causado a la fecha', default='')
    dispc = models.CharField(max_length=64, verbose_name='Disponible a causar', default='')
    montocc = models.CharField(max_length=64, verbose_name='Monto a ceder', default='')
    saldofc = models.CharField(max_length=64, verbose_name='Saldo final', default='') 
    direccionc = models.CharField(max_length=64, verbose_name='Dirección cedente', default='')

#BASE DE DATOS DEL MODULO PRESUPUESTO - CEDENTE
class Receptor(models.Model):
    idr = models.CharField(max_length=100, verbose_name='Id Receptor:', default='')
    partidar = models.CharField(max_length=64, verbose_name='Partida', default='')
    generalr = models.CharField(max_length=64, verbose_name='General', default='')
    espefr = models.CharField(max_length=64, verbose_name='Específicaciones', default='')
    subespefr = models.CharField(max_length=64, verbose_name='Sub-Especialidad', default='')
    denomr = models.CharField(max_length=64, verbose_name='Denomincación', default='')
    presuacorr = models.CharField(max_length=64, verbose_name='Presupuesto acordado', default='')
    caufechar = models.CharField(max_length=64, verbose_name='Causado a la fecha', default='')
    dispr = models.CharField(max_length=64, verbose_name='Disponible a causar', default='')
    montocr = models.CharField(max_length=64, verbose_name='Monto a ceder', default='')
    saldofr = models.CharField(max_length=64, verbose_name='Saldo final', default='') 
    direccionr = models.CharField(max_length=64, verbose_name='Dirección cedente', default='')