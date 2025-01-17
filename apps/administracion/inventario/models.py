from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


tipo_considcion = (("N", "Nuevo"), ("U", "Usado"), ("D", "Deteriorado"))


class TipoArticulo(BaseModel):
    LIST_TYPE_ARTICLE = "listar_type_articulo"
    ADD_TYPE_ARTICLE = "agregar_type_articulo"
    VIEW_TYPE_ARTICLE = "ver_type_articulo"
    CHANGE_TYPE_ARTICLE = "editar_type_articulo"
    DELETE_TYPE_ARTICLE = "eliminar_type_articulo"

    nombre = models.CharField(max_length=180)

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "administracion_tipos_articulos"
        verbose_name = "Tipo de Articulo"
        verbose_name_plural = "Tipos de Articulos"
        ordering = ["-id"]
        permissions = [
            ("listar_type_articulo", "Puede listar tipos de articulos"),
            ("agregar_type_articulo", "Puede agregar tipo de articulo"),
            ("ver_type_articulo", "Puede ver tipo de articulo"),
            ("editar_type_articulo", "Puede actualizar tipo de articulo"),
            ("eliminar_type_articulo", "Puede eliminar tipo de articulo"),
        ]


class Articulo(BaseModel):
    LIST_ARTICLE = "listar_articulo"
    ADD_ARTICLE = "agregar_articulo"
    VIEW_ARTICLE = "ver_articulo"
    CHANGE_ARTICLE = "editar_articulo"
    DELETE_ARTICLE = "eliminar_articulo"

    descripcion = models.TextField(max_length=255)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    placa = models.CharField(max_length=255, blank=True, null=True)
    cantidad_combustible = models.IntegerField(blank=True, null=True)
    codigo_bn = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField()
    tipo_articulo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)
    condicion = models.CharField(max_length=1, choices=tipo_considcion)
    fecha_adq = models.DateField()
    asignado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion + " - " + str(self.marca) + " - " + str(self.modelo)

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "administracion_articulos"
        verbose_name = "Actividad social"
        verbose_name_plural = "Actividades sociales"
        ordering = ["-id"]
        permissions = [
            ("listar_articulo", "Puede listar articulos"),
            ("agregar_articulo", "Puede agregar articulo"),
            ("ver_articulo", "Puede ver articulo"),
            ("editar_articulo", "Puede actualizar articulo"),
            ("eliminar_articulo", "Puede eliminar articulo"),
        ]
