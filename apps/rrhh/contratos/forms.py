from django import forms
from .models import Contrato
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_sede,
    validate_condicion,
    validate_nombres_apellidos,
    validate_ente,
)


class ContratoForm(FormBase):
    fecha_ingreso_911 = FormBase.create_date_field(
        "fecha_ingreso_911", title="Fecha Ingreso 911"
    )
    fecha_ingreso_apn = FormBase.create_date_field(
        "fecha_ingreso_apn", title="Fecha Ingreso APN"
    )
    fecha_ingreso = FormBase.create_date_field("fecha_ingreso", title="Fecha Ingreso")
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion", title="Fecha Culminacion"
    )

    class Meta:
        model = Contrato
        fields = (
            "tipo",
            "comision_servicio",
            "pnb",
            "departamento",
            "tipo_personal",
            "cargo",
            "sede",
            "fecha_ingreso_911",
            "fecha_ingreso_apn",
            "fasmij",
            "fecha_ingreso",
            "fecha_culminacion",
            "empleado",
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
            "tipo": "Tipo de contrato",
            "cargo": "Cargo asignado",
            "empleado": "Nombre del empleado",
        }
        widgets = {}

    # Validaciones de texto
    def clean_departamento(self):
        data = self.cleaned_data.get("departamento")
        validate_sede(
            data, "El departamento solo puede contener letras, números y espacios"
        )
        return data

    def clean_sede(self):
        data = self.cleaned_data.get("sede")
        validate_sede(data, "La sede solo puede contener letras, números y espacios")
        return data

    def clean_cargo(self):
        data = self.cleaned_data.get("cargo")
        validate_ente(
            data, "El cargo solo permite letras, números y caracteres .,-!?()"
        )
        return data

    def clean_tipo(self):
        data = self.cleaned_data.get("tipo")
        validate_condicion(
            data,
            "El tipo de contrato solo permite letras, números y caracteres básicos",
        )
        return data

    def clean_tipo_personal(self):
        data = self.cleaned_data.get("tipo_personal")
        validate_condicion(
            data,
            "El tipo de personal solo permite letras, números y caracteres básicos",
        )
        return data

    def clean_empleado(self):
        data = self.cleaned_data.get("empleado")
        validate_nombres_apellidos(
            data, "El nombre debe contener solo letras y espacios"
        )
        return data

    # Validaciones booleanas optimizadas
    def clean_comision_servicio(self):
        return self.cleaned_data.get("comision_servicio") or False

    def clean_pnb(self):
        return self.cleaned_data.get("pnb") or False

    def clean_fasmij(self):
        return self.cleaned_data.get("fasmij") or False

    # Validación de fechas
    def clean(self):
        cleaned_data = super().clean()
        fecha_ingreso = cleaned_data.get("fecha_ingreso")
        fecha_culminacion = cleaned_data.get("fecha_culminacion")

        if fecha_ingreso and fecha_culminacion:
            if fecha_culminacion < fecha_ingreso:
                self.add_error(
                    "fecha_culminacion",
                    "La fecha de culminación no puede ser anterior a la fecha de ingreso",
                )

        # Validación adicional para fecha_ingreso_911 y fecha_ingreso_apn
        fecha_911 = cleaned_data.get("fecha_ingreso_911")
        fecha_apn = cleaned_data.get("fecha_ingreso_apn")

        if fecha_911 and fecha_apn and fecha_apn < fecha_911:
            self.add_error(
                "fecha_ingreso_apn",
                "La fecha de ingreso APN no puede ser anterior al ingreso 911",
            )

        return cleaned_data
