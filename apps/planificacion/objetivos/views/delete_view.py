from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import ObjetivoForm
from ..models import Objetivo
from ..services import ObjetivoService


class ObjetivoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Objetivos"
        context["titleForm"] = "Eliminar objetivo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("objetivos:list")
        context["urlDelete"] = reverse_lazy(
            "api_objetivos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Objetivo.objects.filter(pk=id)


class ObjetivoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = ObjetivoForm

    def __init__(self):
        self.service = ObjetivoService()
