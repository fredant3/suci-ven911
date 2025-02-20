from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from rrhh.tipos_empleados.forms import TipoEmpleadoForm
from rrhh.tipos_empleados.models import TipoEmpleado
from rrhh.tipos_empleados.services import TipoEmpleadoService


class TipoEmpleadoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "rrhh.tipos_empleados.editar_tipo_empleado"
    form_class = TipoEmpleadoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
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
    permission_required = "rrhh.tipos_empleados.editar_tipo_empleado"
    form_class = TipoEmpleadoForm

    def __init__(self):
        self.service = TipoEmpleadoService()
