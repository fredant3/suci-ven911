from administracion.departamentos.models import Departamento
from administracion.inventario.models import Articulo
from administracion.sedes.models import Sede
from django.db import models
from helpers.BaseModelMixin import BaseModel
from users.auth.models import User


class Asignacion(BaseModel):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    observaciones = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
