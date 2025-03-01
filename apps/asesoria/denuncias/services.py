from asesoria.denuncias.repositories import (
    DenunciadoRepository,
    DenuncianteRepository,
    DenunciaRepository,
)
from helpers.CrudMixin import CrudService


class DenunciaService(CrudService):
    denunciante_fields = [
        ("nombres", "nombres_denunciante"),
        ("apellidos", "apellidos_denunciante"),
        ("cedula", "cedula_denunciante"),
        ("telefono", "telefono_denunciante"),
        ("email", "email_denunciante"),
        ("direccion", "direccion_denunciante"),
    ]
    denunciado_fields = [
        ("nombres", "nombres_denunciante"),
        ("apellidos", "apellidos_denunciante"),
        ("cedula", "cedula_denunciante"),
        ("telefono", "telefono_denunciante"),
        ("email", "email_denunciado"),
    ]

    def __init__(self):
        self.repository_denunciante = DenuncianteRepository()
        self.repository_denunciado = DenunciadoRepository()
        self.repository = DenunciaRepository()

    def create_denunciante(self, data):
        payload = self.change_key_create(self.denunciante_fields, data)
        return self.repository_denunciante.create(payload)

    def create_denunciado(self, data):
        payload = self.change_key_create(self.denunciado_fields, data)
        return self.repository_denunciado.create(payload)

    def before_create(self, data):
        payload = {}
        payload["estatus"] = data["estatus"]
        payload["ente"] = data["ente"]
        payload["motivo"] = data["motivo"]
        payload["zona"] = data["zona"]
        payload["fecha_denuncia"] = data["fecha_denuncia"]
        payload["fecha_incidente"] = data["fecha_incidente"]

        payload["denunciante"] = self.create_denunciante(data)
        payload["denunciado"] = self.create_denunciado(data)

        return payload

    def update_denunciante(self, entity, data):
        data = self.change_key_update(self.denunciante_fields, data)
        return self.repository_denunciante.update(entity, data)

    def update_denunciado(self, entity, data):
        data = self.change_key_update(self.denunciado_fields, data)
        return self.repository_denunciado.update(entity, data)

    def before_update(self, entity, data):
        self.update_denunciante(entity.denunciante, data)
        self.update_denunciado(entity.denunciado, data)
