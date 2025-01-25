from helpers.FormBase import FormBase
from seguridad.vehiculos.models import Vehiculo


class VehiculoForm(FormBase):
    fecha = FormBase.create_date_field("fecha")
    hora = FormBase.create_time_field("hora")

    class Meta:
        model = Vehiculo
        fields = (
            "nombre",
            "apellido",
            "cedula",
            "modelo",
            "vehiculo",
            "motivo",
            "cantigasolina",
            "placa",
            "fecha",
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
