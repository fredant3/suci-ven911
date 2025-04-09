from potencia.uri.models import Uri
from helpers.FormBase import FormBase


class UriInfoGeneralForm(FormBase):
    class Meta:
        model = Uri
        fields = ("nroreporte",)


class UripacienteForm(FormBase):
    class Meta:
        model = Uri
        fields = ("nombrepaciente",)


class UriConsentimientoForm(FormBase):
    class Meta:
        model = Uri
        fields = ("nombre_acompanante",)


class UriDireccionForm(FormBase):
    class Meta:
        model = Uri
        fields = ("sector_evento",)
