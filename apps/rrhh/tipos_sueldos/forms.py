from django import forms
from rrhh.tipos_sueldos.models import TipoSueldo
from helpers.FormBase import FormBase
from helpers.validForm import validate_valor_bs, validate_observaciones


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
            "tipo": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione tipo de sueldo",
                }
            ),
            "monto": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "0.00", "step": "0.01"}
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

    def clean_tipo(self):
        data = self.cleaned_data.get("tipo")
        valid_types = [choice[0] for choice in TipoSueldo.TIPO_CHOICES]
        if data not in valid_types:
            raise forms.ValidationError("Seleccione un tipo de sueldo válido")
        return data

    def clean_monto(self):
        data = self.cleaned_data.get("monto")
        validate_valor_bs(
            str(data), "El monto debe ser un valor positivo con hasta dos decimales"
        )
        return data

    def clean_descripcion(self):
        data = self.cleaned_data.get("descripcion")
        validate_observaciones(data, "La descripción contiene caracteres no permitidos")
        return data

    def clean_estatus(self):
        data = self.cleaned_data.get("estatus")
        valid_status = [choice[0] for choice in TipoSueldo.ESTATUS_CHOICES]
        if data not in valid_status:
            raise forms.ValidationError("Seleccione un estatus válido")
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
                self.add_error(None, "Esta combinación de tipo y estatus ya existe")

        return cleaned_data
