# from administracion.averia.forms import AveriaForm
from apps.reporte.reportes_administracion.forms import ReportesAdministracionForm

# from administracion.averia.services import AveriaService
from apps.reporte.reportes_administracion.services import ReportesAdministracionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class ReportesAdministracionCreateView(
    LoginRequiredMixin, CheckPermisosMixin, CreateView
):
    permission_required = "reporte.reportes_administracion.agregar_reporte"

    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Reporte"
        context["indexUrl"] = reverse_lazy("reporte:index")
        context["module"] = "Reporte"
        context["submodule"] = "reportes_administracion"
        context["titleForm"] = "Registrar un nuevo reporte"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("reportes_administracion:list")
        context["urlForm"] = reverse_lazy("api_reportes_administracion:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ReportesAdministracionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "reporte.reportes_administracion.agregar_reporte"
    form_class = ReportesAdministracionForm

    def __init__(self):
        self.service = ReportesAdministracionService()
