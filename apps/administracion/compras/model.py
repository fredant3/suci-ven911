from administracion.inventario.models import Articulo
from django.db import models
from helpers.BaseModelMixin import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Compra(BaseModel):
    articulo = models.ForeignKey(
        Articulo, on_delete=models.CASCADE, verbose_name="Artículo"
    )
    n_orden = models.IntegerField(
        "N° de orden",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(999999999),
        ],
    )
    valor_bs = models.TextField("Valor en BS", max_length=255)

    class Meta:
        permissions = [
            ("listar_compra", "Puede listar compras"),
            ("agregar_compra", "Puede agregar compra"),
            ("ver_compra", "Puede ver compra"),
            ("editar_compra", "Puede actualizar compra"),
            ("eliminar_compra", "Puede eliminar compra"),
        ]
