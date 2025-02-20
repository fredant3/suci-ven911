import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.tipos_empleados.services import TipoEmpleadoService


class TipoEmpleadoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.tipos_empleados.listar_tipo_empleado"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Tipos de Empleados"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("tipos_empleados:create")
        context["listApiUrl"] = reverse_lazy("api_tipos_empleados:list")
        context["updateUrl"] = reverse_lazy("tipos_empleados:update", args=[0])
        context["deleteUrl"] = reverse_lazy("tipos_empleados:delete", args=[0])
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
                "data": "tipo_personal",
                "name": "tipo_personal",
                "title": "Tipo Personal",
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


class TipoEmpleadoListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.tipos_empleados.listar_tipo_empleado"

    def __init__(self):
        self.service = TipoEmpleadoService()
