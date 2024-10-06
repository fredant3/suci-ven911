from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import TipoSueldoForm
from ..services import TipoSueldoService


class TipoSueldoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = TipoSueldoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Tipos de Sueldos"
        context["titleForm"] = "Añadir una tipo de empleado nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("tipos_sueldos:list")
        context["urlForm"] = reverse_lazy("api_tipos_sueldos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class TipoSueldoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = TipoSueldoForm

    def __init__(self):
        self.service = TipoSueldoService()
