# from administracion.averia.forms import AveriaForm
from apps.reporte.reportes_administracion.forms import ReportesAdministracionForm

# from administracion.averia.models import Averia
from apps.reporte.reportes_administracion.models import ReportesAdministracion

# from administracion.averia.services import AveriaService
from apps.reporte.reportes_administracion.services import ReportesAdministracionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class ReportesAdministracionUpdateView(
    LoginRequiredMixin, CheckPermisosMixin, UpdateView
):
    permission_required = "reporte.reportes_administracion.editar_reporte"
    form_class = ReportesAdministracionForm

    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Reporte"
        context["indexUrl"] = reverse_lazy("reporte")
        context["module"] = "Reporte"
        context["submodule"] = "reportes_administracion"
        context["titleForm"] = "Editar reporte"
        context["tag"] = "Guardar cambios"
        context["listUrl"] = reverse_lazy("reportes_administracion:list")
        context["urlForm"] = reverse_lazy(
            "api_reportesadministracion:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return ReportesAdministracion.objects.filter(pk=id)


class ReportesAdministracionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "reporte.reportes_administracion.editar_reporte"
    form_class = ReportesAdministracionForm

    def __init__(self):
        self.service = ReportesAdministracionService()
