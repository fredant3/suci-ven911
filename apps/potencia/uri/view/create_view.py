from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from formtools.wizard.views import SessionWizardView
from potencia.uri.forms import (
    UriInfoGeneralForm,
    UripacienteForm,
    UriConsentimientoForm,
    UriDireccionForm,
    UriInfoclinicaForm,
    UriSignosVitalesForm,
    UriReferenciasForm,
)

from templates.sneat import TemplateLayout

from potencia.uri.services import UriService
from django.http import HttpResponse


class UriCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "potencia.uri.agregar_uri"
    form_class = UriInfoGeneralForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        context["titleForm"] = "Añadir registro"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("uri:list")
        context["urlForm"] = reverse_lazy("api_uri:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class UriCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "potencia.uri.agregar_uri"
    form_class = UriInfoGeneralForm


class InfogeneralWizardView(SessionWizardView):
    template_name = "widzard/index.html"
    form_list = [
        UriInfoGeneralForm,
        UripacienteForm,
        UriConsentimientoForm,
        UriDireccionForm,
        UriInfoclinicaForm,
        UriSignosVitalesForm,
        UriReferenciasForm,
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        return TemplateLayout.init(self, context)

    def done(self, form_list, **kwargs):
        print (form_list)
        return HttpResponse()

    # def __init__(self):
    # self.service = UriService()
