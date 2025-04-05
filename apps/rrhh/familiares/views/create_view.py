from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from rrhh.familiares.forms import FamiliarForm
from rrhh.familiares.services import FamiliarService


class FamiliarCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "rrhh.familiares.agregar_familiar"
    form_class = FamiliarForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Familiares"
        context["titleForm"] = "Añadir un Familiar Nuevo"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("familiares:list")
        context["urlForm"] = reverse_lazy("api_familiares:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class FamiliarCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "rrhh.familiares.agregar_familiar"
    form_class = FamiliarForm

    def __init__(self):
        self.service = FamiliarService()
