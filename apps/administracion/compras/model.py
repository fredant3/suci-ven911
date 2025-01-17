from administracion.inventario.models import Articulo
from django.db import models
from helpers.BaseModelMixin import BaseModel
from users.auth.models import User


class Compra(BaseModel):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    n_orden = models.IntegerField()
    valor_bs = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
