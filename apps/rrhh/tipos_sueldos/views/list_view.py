import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.tipos_sueldos.services import TipoSueldoService


class TipoSueldoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.tipos_sueldos.listar_tipo_sueldo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion Humana"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Gestion Humana"
        context["submodule"] = "Tipos de Sueldos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("tipos_sueldos:create")
        context["listApiUrl"] = reverse_lazy("api_tipos_sueldos:list")
        context["updateUrl"] = reverse_lazy("tipos_sueldos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("tipos_sueldos:delete", args=[0])
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
                "data": "tipo",
                "name": "tipo",
                "title": "Tipo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "monto",
                "name": "monto",
                "title": "Monto",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class TipoSueldoListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.tipos_sueldos.listar_tipo_sueldo"

    def __init__(self):
        self.service = TipoSueldoService()
