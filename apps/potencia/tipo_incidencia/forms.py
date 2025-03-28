from django import forms
from potencia.tipo_incidencia.models import TipoIncidencia
from helpers.FormBase import FormBase
from helpers.validForm import validate_basic_text


class TipoIncidenciaForm(FormBase):
    class Meta:
        model = TipoIncidencia
        fields = ["tipo"]
        labels = {
            "tipo": "Tipo de Incidencia",
        }
        widgets = {
            "tipo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: Fallo eléctrico"}
            ),
        }

    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")

        # Validación de formato
        validate_basic_text(
            tipo,
            "El tipo de incidencia solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )

        # Validación de unicidad
        if TipoIncidencia.objects.filter(tipo__iexact=tipo).exists():
            raise forms.ValidationError("Este tipo de incidencia ya existe")

        return tipo
