import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import InfraestructuraService


class InfraestructuraListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "planificacion.infraestructuras.listar_infraestructuras"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Infraestructuras"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("infraestructuras:create")
        context["listApiUrl"] = reverse_lazy("api_infraestructuras:list")
        context["updateUrl"] = reverse_lazy("infraestructuras:update", args=[0])
        context["deleteUrl"] = reverse_lazy("infraestructuras:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_infraestructuras:export_excel")
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
                "searchable": "true",
            },
            {
                "data": "estado",
                "name": "estado",
                "title": "Estado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "mes",
                "name": "mes",
                "title": "Mes",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "infraestructura",
                "name": "infraestructura",
                "title": "Infraestrutuctura (Energía y Potencia)",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cantidad",
                "name": "cantidad",
                "title": "Cantidad",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class InfraestructuraListApiView(ListController, CheckPermisosMixin):
    permission_required = "planificacion.infraestructuras.listar_infraestructuras"

    def __init__(self):
        self.service = InfraestructuraService()
