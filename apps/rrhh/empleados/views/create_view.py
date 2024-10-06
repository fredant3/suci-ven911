from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import EmpleadoForm
from ..services import EmpleadoService


class EmpleadoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = EmpleadoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Empleados"
        context["titleForm"] = "Añadir una empleado nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("empleados:list")
        context["urlForm"] = reverse_lazy("api_empleados:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class EmpleadoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = EmpleadoForm

    def __init__(self):
        self.service = EmpleadoService()
