import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import IncidenciaService


class IncidenciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Incidencias"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("incidencias:create")
        context["listApiUrl"] = reverse_lazy("api_incidencias:list")
        context["updateUrl"] = reverse_lazy("incidencias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("incidencias:delete", args=[0])
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
                "data": "tiposolicitud",
                "name": "tiposolicitud",
                "title": "Tipo de Solicitud",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "usuario",
                "name": "usuario",
                "title": "Usuario",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estado",
                "name": "estado",
                "title": "Estado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "sede",
                "name": "sede",
                "title": "Sede",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "departamento",
                "name": "departamento",
                "title": "Departamento",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "tipoincidencia",
                "name": "tipoincidencia",
                "title": "Tipo de Incidencia",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "observaciones",
                "name": "observaciones",
                "title": "Observaciones",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class IncidenciaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = IncidenciaService()
