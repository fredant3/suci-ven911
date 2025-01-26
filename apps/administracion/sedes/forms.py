from helpers.FormBase import FormBase

from .models import Sede


class SedeForm(FormBase):
    class Meta:
        model = Sede
        fields = (
            "sede",
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
