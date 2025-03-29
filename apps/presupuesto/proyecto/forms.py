from helpers.FormBase import FormBase
from presupuesto.proyecto.models import Proyecto
from django import forms
from helpers.validForm import (
    validate_general_text,
    validate_decimal_number,
    validate_nombres_apellidos,
    validate_basic_text,
)


class ProyectoForm(FormBase):
    fechai = FormBase.create_date_field("fechai", title="Fecha de inicio")
    fechac = FormBase.create_date_field("fechac", title="Fecha de culminacion")

    class Meta:
        model = Proyecto
        fields = (
            "nombrep",
            "fechai",
            "fechac",
            "situacionp",
            "montoproyecto",
            "responsableg",
            "responsablet",
            "responsabler",
            "responsablea",
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
            "nombrep": "Nombre del Proyecto",
            "montoproyecto": "Monto del Proyecto",
            "situacionp": "Situación Actual",
        }
        widgets = {
            "nombrep": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del proyecto",
                }
            ),
            "fechai": forms.DateInput(attrs={"class": "form-control datepicker"}),
            "fechac": forms.DateInput(attrs={"class": "form-control datepicker"}),
            "responsableg": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable gerente",
                }
            ),
            "responsablet": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable tecnico",
                }
            ),
            "responsabler": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable registrador",
                }
            ),
            "responsablea": forms.TextInput(
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
            "situacionp": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la situación del proyecto",
                }
            ),
            "montoproyecto": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el monto del proyecto",
                }
            ),
        }

    def clean_nombrep(self):
        nombre = self.cleaned_data.get("nombrep")
        validate_general_text(
            nombre,
            "El nombre del proyecto solo permite letras, números y caracteres .,-!?()",
        )
        return nombre

    def clean_situacionp(self):
        situacion = self.cleaned_data.get("situacionp")
        validate_basic_text(
            situacion, "La situación debe contener letras, números y caracteres .,-"
        )
        return situacion

    def clean_montoproyecto(self):
        monto = self.cleaned_data.get("montoproyecto")
        validate_decimal_number(
            str(monto), "El monto debe ser un valor positivo con hasta dos decimales"
        )
        return monto

    def clean_responsable(self, field_name):
        responsable = self.cleaned_data.get(field_name)
        validate_nombres_apellidos(
            responsable, "Este campo solo permite letras y espacios"
        )
        return responsable

    def clean_responsableg(self):
        return self.clean_responsable("responsableg")

    def clean_responsablet(self):
        return self.clean_responsable("responsablet")

    def clean_responsabler(self):
        return self.clean_responsable("responsabler")

    def clean_responsablea(self):
        return self.clean_responsable("responsablea")

    def clean_estatus(self):
        estatus = self.cleaned_data.get("estatus")
        validate_general_text(
            estatus, "El estatus solo permite letras, números y caracteres .,-!?()"
        )
        return estatus

    def clean(self):
        cleaned_data = super().clean()
        fechai = cleaned_data.get("fechai")
        fechac = cleaned_data.get("fechac")

        if fechai and fechac and fechac < fechai:
            self.add_error(
                "fechac",
                "La fecha de culminación no puede ser anterior a la fecha de inicio",
            )
        return cleaned_data
