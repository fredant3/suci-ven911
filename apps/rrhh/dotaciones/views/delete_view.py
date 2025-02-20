from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from rrhh.dotaciones.forms import DotacionForm
from rrhh.dotaciones.models import Dotacion
from rrhh.dotaciones.services import DotacionService


class DotacionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "rrhh.dotaciones.eliminar_dotacion"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Dotaciones"
        context["titleForm"] = "Eliminar dotacion"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("dotaciones:list")
        context["urlDelete"] = reverse_lazy(
            "api_dotaciones:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Dotacion.objects.filter(pk=id)


class DotacionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "rrhh.dotaciones.eliminar_dotacion"
    form_class = DotacionForm

    def __init__(self):
        self.service = DotacionService()
