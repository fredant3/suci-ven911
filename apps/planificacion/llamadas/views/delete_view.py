from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from planificacion.llamadas.forms import LlamadaForm
from planificacion.llamadas.models import Llamada
from planificacion.llamadas.services import LlamadaService

from templates.sneat import TemplateLayout


class LlamadaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Llamadas"
        context["titleForm"] = "Eliminar llamada"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("llamadas:list")
        context["urlDelete"] = reverse_lazy(
            "api_llamadas:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Llamada.objects.filter(pk=id)


class LlamadaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = LlamadaForm

    def __init__(self):
        self.service = LlamadaService()
