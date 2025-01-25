from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import LlamadaForm
from ..models import Llamada
from ..services import LlamadaService


class LlamadaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = LlamadaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Llamadas"
        context["titleForm"] = "Actualizar llamada"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("llamadas:list")
        context["urlForm"] = reverse_lazy(
            "api_llamadas:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Llamada.objects.filter(pk=id)


class LlamadaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = LlamadaForm

    def __init__(self):
        self.service = LlamadaService()
