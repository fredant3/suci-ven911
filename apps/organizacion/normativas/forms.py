from organizacion.normativas.models import Normativa
from helpers.FormBase import FormBase


class NormativaForm(FormBase):
    date = FormBase.create_date_field("date")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields.pop("file")

    class Meta:
        model = Normativa
        fields = [
            "name",
            "file",
            "date",
            "progre",
            "estado",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
