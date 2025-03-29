from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity

from django.forms import ModelForm
from django.forms.fields import DateTimeInput


class SocialActivityForm(ModelForm):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.fields["location"].widget.attrs.update({"placeholder": "Ingrese la direccion de la actividad"})
        self.fields["reason"].widget.attrs.update({"placeholder": "Ingrese el motivio de la actividad"})
        self.fields["description"].widget.attrs.update({"placeholder": "Ingrese la descripcion"})
        self.fields["beneficiaries"].widget.attrs.update({"placeholder": "Ingrese la cantidad de beneficiarios"})
        for form in self.visible_fields():
            form.field.widget.attrs.update({"class": "form-control", "autocomplete": "off"})

    class Meta:
        model = SocialActivityEntity
        fields = (
            "date",
            "location",
            "activity_type",
            "reason",
            "description",
            "beneficiaries",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "delete_at",
            "delete_by",
        ]
        widgets = {
            "date": DateTimeInput(
                attrs={
                    "type": "date",
                    "placeholder": "Ingrese la fecha de la actividad",
                }
            ),
        }
