from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import TipoEmpleadoForm
from ..services import TipoEmpleadoService


class TipoEmpleadoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = TipoEmpleadoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Tipos de Empleados"
        context["titleForm"] = "Añadir una tipo de empleado nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("tipos_empleados:list")
        context["urlForm"] = reverse_lazy("api_tipos_empleados:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class TipoEmpleadoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = TipoEmpleadoForm

    def __init__(self):
        self.service = TipoEmpleadoService()
