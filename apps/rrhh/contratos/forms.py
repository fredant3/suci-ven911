from django import forms

from .models import Contrato
from helpers.FormBase import FormBase


class ContratoForm(FormBase):
    fecha_ingreso_911 = FormBase.create_date_field(
        "fecha_ingreso_911", "Fecha Ingreso 911"
    )
    fecha_ingreso_apn = FormBase.create_date_field(
        "fecha_ingreso_apn", "Fecha Ingreso APN"
    )
    fecha_ingreso = FormBase.create_date_field("fecha_ingreso", "Fecha Ingreso")
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion", "Fecha Culminacion"
    )

    def clean_comision_servicio(self):
        print("comision_servicio")
        comision_servicio = self.cleaned_data.get("comision_servicio")
        print(comision_servicio)
        print("comision_servicio")
        print("comision_servicio")
        if comision_servicio is None:
            return False
        return comision_servicio

    def clean_pnb(self):
        pnb = self.cleaned_data.get("pnb")
        if pnb is None:
            return False
        return pnb

    def clean_fasmij(self):
        fasmij = self.cleaned_data.get("fasmij")
        if fasmij is None:
            return False
        return fasmij

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
