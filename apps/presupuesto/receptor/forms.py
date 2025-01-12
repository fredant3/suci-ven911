from django import forms

from presupuesto.receptor.models import Receptor


class ReceptorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceptorForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Receptor
        fields = (
            "idr",
            "partidar",
            "generalr",
            "espefr",
            "subespefr",
            "denomr",
            "presuacorr",
            "caufechar",
            "dispr",
            "montocr",
            "saldofr",
            "direccionr",
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
