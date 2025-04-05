from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from gestion_comunicacional.forms import GestionComunicacionalForm
from gestion_comunicacional.models import Gestion_comunicacional
from gestion_comunicacional.services import GestioncomunicacionalService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class EmergenciaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "gestioncomunicacional.eliminar_gestioncomunicacional"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestioncomunicacional"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Gestioncomunicacional"
        context["submodule"] = "Gestioncomunicacional"
        context["titleForm"] = "Eliminar gestioncomunicacional"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("gestioncomunicacional:list")
        context["urlDelete"] = reverse_lazy(
            "api_gestioncomunicacional:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Gestion_comunicacional.objects.filter(pk=id)


class EmergenciaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "emergrncia.eliminar_emergencia"
    form_class = GestionComunicacionalForm

    def __init__(self):
        self.service = GestioncomunicacionalService()
