from django import forms
from rrhh.tipos_sueldos.models import TipoSueldo
from helpers.FormBase import FormBase
from helpers.validForm import validate_decimal_number


class TipoSueldoForm(FormBase):
    class Meta:
        model = TipoSueldo
        fields = (
            "tipo",
            "monto",
            "descripcion",
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
        widgets = {
            "monto": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "0.00",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Compensación por horas extras...",
                    "rows": 3,
                }
            ),
            "estatus": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione estatus"}
            ),
        }
        labels = {
            "tipo": "Tipo de Sueldo",
            "monto": "Monto Asignado",
            "descripcion": "Descripción Detallada",
            "estatus": "Estado Actual",
        }

    def clean_monto(self):
        data = self.cleaned_data.get("monto")
        validate_decimal_number(
            str(data), "El monto debe ser un valor positivo con hasta dos decimales"
        )
        return data

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get("tipo")
        estatus = cleaned_data.get("estatus")

        if tipo and estatus:
            queryset = TipoSueldo.objects.filter(tipo=tipo, estatus=estatus)

            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)

            if queryset.exists():
                self.add_error("tipo", "Esta combinación de tipo y estatus ya existe")

        return cleaned_data
