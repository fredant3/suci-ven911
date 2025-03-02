from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from rrhh.empleados.forms import EmpleadoForm
from rrhh.empleados.models import Empleado
from rrhh.empleados.services import EmpleadoService


class EmpleadoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "rrhh.empleados.editar_empleado"
    form_class = EmpleadoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Empleados"
        context["titleForm"] = "Actualizar empleado"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("empleados:list")
        context["urlForm"] = reverse_lazy(
            "api_empleados:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Empleado.objects.filter(pk=id)


class EmpleadoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "rrhh.empleados.editar_empleado"
    form_class = EmpleadoForm

    def __init__(self):
        self.service = EmpleadoService()
