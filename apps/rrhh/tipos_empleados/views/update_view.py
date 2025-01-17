from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import TipoEmpleadoForm
from ..models import TipoEmpleado
from ..services import TipoEmpleadoService


class TipoEmpleadoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = TipoEmpleadoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Tipos de Empleados"
        context["titleForm"] = "Actualizar tipo de empleado"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("tipos_empleados:list")
        context["urlForm"] = reverse_lazy(
            "api_tipos_empleados:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoEmpleado.objects.filter(pk=id)


class TipoEmpleadoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = TipoEmpleadoForm

    def __init__(self):
        self.service = TipoEmpleadoService()
