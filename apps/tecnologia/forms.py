from tecnologia.models import Tecnologia
from tecnologia.models import Inventory
from helpers.FormBase import FormBase


class TecnologiaForm(FormBase):
    class Meta:
        model = Inventory
        fields = ("nombre",
                  "n_activo",
                  "marca",
                  "serial",
                  "color",
                  "estado_conservacion",
                  "descripcion_equipo",
                  "descripcion_ubicacion",
                  "ubicacion",
                  "cantidad",
                  )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
