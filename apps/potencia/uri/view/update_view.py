from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from potencia.uri.models import Uri
from potencia.uri.services import UriService

from templates.sneat import TemplateLayout

from ..forms import (
    UriInfoGeneralForm,
    UriInfolegalForm,
    UripacienteForm,
    UriConsentimientoForm,
    UriDireccionForm,
    UriInfoclinicaForm,
    UriSignosVitalesForm,
    UriReferenciasForm,
)


class UriUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "potencia.uri.editar_uri"
    form_class = UripacienteForm

    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "URI"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "URI"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        context["titleForm"] = "Actualizar registro"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("uri:list")
        context["urlForm"] = reverse_lazy(
            "api_uri:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Uri.objects.filter(pk=id)


class UriUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "potencia.uri.editar_uri"
    form_class = UripacienteForm

    def __init__(self):
        self.service = UriService()
