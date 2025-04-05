from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from gestion_comunicacional.forms import GestionComunicacionalForm
from gestion_comunicacional.models import Gestion_comunicacional
from gestion_comunicacional.services import GestioncomunicacionalService


class EmergenciaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "gestioncomunicacional.actualizar_gestioncomunicacional"
    form_class = GestionComunicacionalForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestioncomunicacional"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Gestioncomunicacional"
        context["submodule"] = "Gestioncomunicacional"
        context["titleForm"] = "Actualizar gestioncomunicacional"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gestioncomunicacional:list")
        context["urlForm"] = reverse_lazy(
            "api_gestioncomunicacional:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Gestion_comunicacional.objects.filter(pk=id)


class Gestion_comunicacionalUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "emergrncia.actualizar_emergencia"
    form_class = GestionComunicacionalForm

    def __init__(self):
        self.service = GestioncomunicacionalService()
