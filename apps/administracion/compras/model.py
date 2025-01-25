from administracion.inventario.models import Articulo
from django.db import models
from helpers.BaseModelMixin import BaseModel


class Compra(BaseModel):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    n_orden = models.IntegerField()
    valor_bs = models.IntegerField()
