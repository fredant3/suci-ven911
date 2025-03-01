from helpers.FormBase import FormBase
from seguridad.salidas.models import Salida


class SalidaForm(FormBase):
    fecha = FormBase.create_date_field("fecha")
    hora = FormBase.create_time_field("hora")

    class Meta:
        model = Salida
        fields = (
            "name",
            "apellido",
            "cedula",
            "telefono",
            "fecha",
            "direccion",
            "cargo",
            "hora",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
