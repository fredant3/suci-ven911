from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from rrhh.educaciones.forms import EducacionForm
from rrhh.educaciones.services import EducacionService


class EducacionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "rrhh.educacion.agregar_educacion"
    form_class = EducacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Educación"
        context["titleForm"] = "Añadir una educación nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("educaciones:list")
        context["urlForm"] = reverse_lazy("api_educaciones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class EducacionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "rrhh.educacion.agregar_educacion"
    form_class = EducacionForm

    def __init__(self):
        self.service = EducacionService()
