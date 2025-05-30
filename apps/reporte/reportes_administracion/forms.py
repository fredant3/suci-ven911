# from administracion.averia.models import Averia
from apps.reporte.reportes_administracion.models import ReportesAdministracion
from helpers.FormBase import FormBase
from django.forms import TextInput, Select


class ReportesAdministracionForm(FormBase):
    class Meta:
        model = ReportesAdministracion
        fields = [
            "problema",
            "tipo_averia",
            "departamento",
            "serial",
            "codigo_bn",
            "observaciones",
            "quien_reporta",
        ]
        widgets = {
            "problema": TextInput(
                attrs={"placeholder": "Describa el problema (mínimo 9 caracteres)"}
            ),
            "serial": TextInput(
                attrs={"placeholder": "Ingrese el número de serie (6-30 caracteres)"}
            ),
            "codigo_bn": TextInput(
                attrs={"placeholder": "Ingrese el código BN (6-30 caracteres)"}
            ),
            "observaciones": TextInput(
                attrs={"placeholder": "Ingrese observaciones (mínimo 10 caracteres)"}
            ),
            "quien_reporta": Select(attrs={"class": "form-select mb-13"}),
        }
