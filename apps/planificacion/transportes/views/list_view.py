import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import TransporteService


class TransporteListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "planificacion.transportes.listar_transportes"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Transportes"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("transportes:create")
        context["listApiUrl"] = reverse_lazy("api_transportes:list")
        context["updateUrl"] = reverse_lazy("transportes:update", args=[0])
        context["deleteUrl"] = reverse_lazy("transportes:delete", args=[0])
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
                "data": "transporte",
                "name": "transporte",
                "title": "Transporte",
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


class TransporteListApiView(ListController, CheckPermisosMixin):
    permission_required = "planificacion.transportes.listar_transportes"

    def __init__(self):
        self.service = TransporteService()
