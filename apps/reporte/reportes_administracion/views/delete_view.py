# from administracion.averia.forms import AveriaForm
from apps.reporte.reportes_administracion.forms import ReportesAdministracionForm

# from administracion.averia.models import Averia
from apps.reporte.reportes_administracion.models import ReportesAdministracion

# from administracion.averia.services import AveriaService
from apps.reporte.reportes_administracion.services import ReportesAdministracionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class ReportesAdministracionDeleteView(
    LoginRequiredMixin, CheckPermisosMixin, DeleteView
):
    permission_required = "reporte.reportes_administracion.eliminar_reporte"

    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Reporte"
        context["indexUrl"] = reverse_lazy("reporte")
        context["module"] = "Reporte"
        context["submodule"] = "reportes_administracion"
        context["titleForm"] = "Confirmar eliminación"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("reportes_administracion:list")
        context["urlDelete"] = reverse_lazy(
            "api_reportesadministracion:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return ReportesAdministracion.objects.filter(pk=id)


class ReportesAdministracionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "reporte.reportes_administracion.eliminar_reporte"
    form_class = ReportesAdministracionForm

    def __init__(self):
        self.service = ReportesAdministracionService()
