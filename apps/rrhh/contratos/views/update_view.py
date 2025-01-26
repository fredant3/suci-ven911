from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import ContratoForm
from ..models import Contrato
from ..services import ContratoService


class ContratoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = ContratoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Contratos"
        context["titleForm"] = "Actualizar contrato"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("contratos:list")
        context["urlForm"] = reverse_lazy(
            "api_contratos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Contrato.objects.filter(pk=id)


class ContratoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ContratoForm

    def __init__(self):
        self.service = ContratoService()
