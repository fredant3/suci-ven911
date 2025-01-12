from helpers.FormBase import FormBase
from seguridad.gestiones.models import Gestion


class GestionForm(FormBase):
    fecha = FormBase.create_date_field("fecha")
    hora = FormBase.create_time_field("hora")

    class Meta:
        model = Gestion
        fields = (
            "name",
            "apellido",
            "cedula",
            "tipo",
            "descripcion",
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
