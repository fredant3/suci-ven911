from administracion.departamentos.models import Departamento
from django.db.models import CASCADE, CharField, ForeignKey, TextField
from helpers.BaseModelMixin import BaseModel
from users.auth.models import User


class TipoAveria(BaseModel):
    nombre = CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Averia(BaseModel):
    problema = TextField(max_length=255)
    tipo_averia = ForeignKey(TipoAveria, on_delete=CASCADE)
    departamento = ForeignKey(Departamento, on_delete=CASCADE)
    ubicacion = TextField(max_length=255)
    serial = CharField(max_length=255)
    codigo_bn = CharField(max_length=255)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.problema
