from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import TipoEmpleadoForm
from ..models import TipoEmpleado
from ..services import TipoEmpleadoService


class TipoEmpleadoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Tipos de Empleados"
        context["titleForm"] = "Eliminar tipo de empleado"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("tipos_empleados:list")
        context["urlDelete"] = reverse_lazy(
            "api_tipos_empleados:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoEmpleado.objects.filter(pk=id)


class TipoEmpleadoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = TipoEmpleadoForm

    def __init__(self):
        self.service = TipoEmpleadoService()
