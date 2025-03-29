from gestion_comunicacional.equipments.entities.EquipmentEntity import EquipmentEntity

from django.forms import ModelForm


class EquipmentForm(ModelForm):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.fields["name"].widget.attrs.update({"placeholder": "Ingrese el equipo (Marca, Modelo)"})
        self.fields["description"].widget.attrs.update({"placeholder": "Ingrese la descripcion"})
        for form in self.visible_fields():
            form.field.widget.attrs.update({"class": "form-control", "autocomplete": "off"})

    class Meta:
        model = EquipmentEntity
        fields = (
            "name",
            "description",
            "status",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "delete_at",
            "delete_by",
        ]
        widgets = {}
