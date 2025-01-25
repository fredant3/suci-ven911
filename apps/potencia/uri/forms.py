from potencia.uri.models import Uri
from helpers.FormBase import FormBase


class UriForm(FormBase):
    class Meta:
        model = Uri
        fields = ("nombre_apellido",)
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
