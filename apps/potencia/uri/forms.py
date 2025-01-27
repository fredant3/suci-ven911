from potencia.uri.models import Uri
from helpers.FormBase import FormBase

fecha_atencion = FormBase.create_date_field("fecha_atencion")


class UriForm(FormBase):
    class Meta:
        model = Uri
        fields = (
            "fecha_atencion",
            "nroreporte",
            "placa",
            "institucion",
            "tipounidad",
            "num_interna",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
