from helpers.FormBase import FormBase

from presupuesto.proyecto.models import Proyecto


class ProyectoForm(FormBase):
    fechai = FormBase.create_date_field("fechai")
    fechac = FormBase.create_date_field("fechac")

    class Meta:
        model = Proyecto
        fields = (
            "nombrep",
            "fechai",
            "fechac",
            "situacionp",
            "montoproyecto",
            "responsableg",
            "responsablet",
            "responsabler",
            "responsablea",
            "estatus",
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
