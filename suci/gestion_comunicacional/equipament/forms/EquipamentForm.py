from django.forms import ModelForm
from gestion_comunicacional.equipament.entities.EquipamentEntity import EquipamentEntity


class EquipamentForm(ModelForm):
    class Meta:
        model = EquipamentEntity
        fields = (
            "name",
            "description",
            "status",
        )
