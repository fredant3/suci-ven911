from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import EmpleadoForm
from ..models import Empleado
from ..services import EmpleadoService


class EmpleadoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "rrhh.empleados.eliminar_empleado"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Empleados"
        context["titleForm"] = "Eliminar empleado"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("empleados:list")
        context["urlDelete"] = reverse_lazy(
            "api_empleados:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Empleado.objects.filter(pk=id)


class EmpleadoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "rrhh.empleados.eliminar_empleado"
    form_class = EmpleadoForm

    def __init__(self):
        self.service = EmpleadoService()
