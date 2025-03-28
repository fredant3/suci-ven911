from django import forms
from presupuesto.models import Accion
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_valor_bs,
    validate_nombres_apellidos,
    validate_condicion,
    validate_ente,
)


class AccionForm(FormBase):
    fecha_inicio = FormBase.create_date_field("fecha_inicio", title="Fecha Inicio")
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion", title="Fecha Culminacion"
    )

    class Meta:
        model = Accion
        fields = (
            "proyecto",
            "fecha_inicio",
            "fecha_culminacion",
            "situacion_presupuestaria",
            "monto",
            "responsable_gerente",
            "responsable_tecnico",
            "responsable_registrador",
            "responsable_administrativo",
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
        labels = {
            "situacion_presupuestaria": "Situación Presupuestaria",
            "monto": "Monto asignado",
        }
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control datepicker"}),
            "fecha_culminacion": forms.DateInput(
                attrs={"class": "form-control datepicker"}
            ),
            "proyecto": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del proyecto",
                }
            ),
            "responsable_gerente": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable gerente",
                }
            ),
            "responsable_tecnico": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable tecnico",
                }
            ),
            "responsable_registrador": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable registrador",
                }
            ),
            "responsable_administrativo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable administrativo",
                }
            ),
            "estatus": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el estatus",
                }
            ),
        }

    def clean_monto(self):
        monto = self.cleaned_data.get("monto")
        validate_valor_bs(
            str(monto), "El monto debe ser un valor positivo con hasta dos decimales"
        )
        return monto

    def clean_responsable(self, field_name):
        nombre = self.cleaned_data.get(field_name)
        validate_nombres_apellidos(
            nombre, "Este campo solo puede contener letras y espacios"
        )
        return nombre

    def clean_responsable_gerente(self):
        return self.clean_responsable("responsable_gerente")

    def clean_responsable_tecnico(self):
        return self.clean_responsable("responsable_tecnico")

    def clean_responsable_registrador(self):
        return self.clean_responsable("responsable_registrador")

    def clean_responsable_administrativo(self):
        return self.clean_responsable("responsable_administrativo")

    def clean_situacion_presupuestaria(self):
        situacion = self.cleaned_data.get("situacion_presupuestaria")
        validate_condicion(
            situacion, "Use solo letras, números, espacios y los caracteres .,-."
        )
        return situacion

    def clean_estatus(self):
        estatus = self.cleaned_data.get("estatus")
        validate_ente(
            estatus,
            "El estatus solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return estatus

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_culminacion = cleaned_data.get("fecha_culminacion")

        if fecha_inicio and fecha_culminacion:
            if fecha_culminacion < fecha_inicio:
                self.add_error(
                    "fecha_culminacion",
                    "La fecha de culminación no puede ser anterior a la fecha de inicio",
                )

        return cleaned_data
