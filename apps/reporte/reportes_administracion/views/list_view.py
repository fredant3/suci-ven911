import json

# from administracion.averia.services import AveriaService
from apps.reporte.reportes_administracion.services import ReportesAdministracionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout


class ReportesAdministracionListView(
    LoginRequiredMixin, CheckPermisosMixin, TemplateView
):
    permission_required = "reporte.reportesadministracion.listar_reportesadministracion"

    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Reporte"
        context["indexUrl"] = reverse_lazy("index")
        context["module"] = "Reporte"
        context["submodule"] = "reportes_administracion"
        context["createBtn"] = "Nueva avería"
        context["createUrl"] = reverse_lazy("reportes_administracion:create")
        context["listApiUrl"] = reverse_lazy("api_reportes_administracion:list")
        context["updateUrl"] = reverse_lazy("reportes_administracion:update", args=[0])
        context["deleteUrl"] = reverse_lazy("reportes_administracion:delete", args=[0])
        # context["exportExcelUrl"] = reverse_lazy("reportes_administracion:export_excel")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "problema",
                "name": "problema",
                "title": "Problema",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "tipo_averia__nombre",
                "name": "tipo_averia__nombre",
                "title": "Tipo de avería",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "departamento__nombre",
                "name": "departamento__nombre",
                "title": "Departamento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "serial",
                "name": "serial",
                "title": "Número de serie",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "codigo_bn",
                "name": "codigo_bn",
                "title": "Código BN",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "quien_reporta",
                "name": "quien_reporta",
                "title": "Departamento Averia",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class ReportesAdministracionListApiView(ListController, CheckPermisosMixin):
    permission_required = "reporte.reportesadministracion.listar_reportesadministracion"

    def __init__(self):
        self.service = ReportesAdministracionService()
