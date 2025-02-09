from administracion.departamentos.models import Departamento
from django.db.models import CASCADE, CharField, ForeignKey, TextField
from helpers.BaseModelMixin import BaseModel


class TipoAveria(BaseModel):
    nombre = CharField(max_length=255)
    permissions = [
        ("listar_tipo_averia", "Puede listar tipos de averias"),
        ("agregar_tipo_averia", "Puede agregar tipo de averia"),
        ("ver_tipo_averia", "Puede ver tipo de averia"),
        ("editar_tipo_averia", "Puede actualizar tipo de averia"),
        ("eliminar_tipo_averia", "Puede eliminar tipo de averia"),
    ]

    def __str__(self):
        return self.nombre


class Averia(BaseModel):
    problema = TextField(max_length=255)
    tipo_averia = ForeignKey(TipoAveria, on_delete=CASCADE)
    departamento = ForeignKey(Departamento, on_delete=CASCADE)
    ubicacion = TextField(max_length=255)
    serial = CharField(max_length=255)
    codigo_bn = CharField(max_length=255)
    permissions = [
        ("listar_averia", "Puede listar averias"),
        ("agregar_averia", "Puede agregar averia"),
        ("ver_averia", "Puede ver averia"),
        ("editar_averia", "Puede actualizar averia"),
        ("eliminar_averia", "Puede eliminar averia"),
    ]

    def __str__(self):
        return self.problema
