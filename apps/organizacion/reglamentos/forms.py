from organizacion.reglamentos.models import Reglamento
from helpers.FormBase import FormBase


class ReglamentoForm(FormBase):
    date = FormBase.create_date_field("date")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields.pop("file")

    class Meta:
        model = Reglamento
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
