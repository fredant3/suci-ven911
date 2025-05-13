import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from presupuesto.traspaso.services import TraspasoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class TraspasoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.traspaso.listar_traspaso"
    url_redirect = reverse_lazy("presupuesto")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("traspasos:create")
        context["listApiUrl"] = reverse_lazy("api_traspasos:list")
        context["updateUrl"] = reverse_lazy("traspasos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("traspasos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_traspasos:export_excel")
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
                "data": "proyecto_acciones",
                "name": "proyecto_acciones",
                "title": "Proyecto o Acción",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class TraspasoListApiView(ListController, CheckPermisosMixin):
    permission_required = "presupuesto.traspaso.listar_traspaso"

    def __init__(self):
        self.service = TraspasoService()
