from administracion.inventario.models import Articulo
from django.db import models
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import PositiveIntegerValidator, CurrencyValidator
from django.core.validators import MinValueValidator


class Compra(BaseModel):
    articulo = models.ForeignKey(
        Articulo, on_delete=models.CASCADE, verbose_name="Artículo"
    )
    n_orden = models.IntegerField(
        "N° de orden",
        validators=[
            MinValueValidator(1),
            PositiveIntegerValidator(),
        ],
    )
    valor_bs = models.TextField(
        "Valor en BS",
        validators=[CurrencyValidator()],
    )

    class Meta:
        permissions = [
            ("listar_compra", "Puede listar compras"),
            ("agregar_compra", "Puede registrar compras"),
            ("ver_compra", "Puede ver detalles de compras"),
            ("editar_compra", "Puede editar compras"),
            ("eliminar_compra", "Puede eliminar compras"),
        ]
