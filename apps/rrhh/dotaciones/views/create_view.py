from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from rrhh.dotaciones.forms import DotacionForm
from rrhh.dotaciones.services import DotacionService


class DotacionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "rrhh.dotaciones.agregar_dotacion"
    form_class = DotacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Dotaciones"
        context["titleForm"] = "Añadir una dotacion nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("dotaciones:list")
        context["urlForm"] = reverse_lazy("api_dotaciones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class DotacionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "rrhh.dotaciones.agregar_dotacion"
    form_class = DotacionForm

    def __init__(self):
        self.service = DotacionService()
