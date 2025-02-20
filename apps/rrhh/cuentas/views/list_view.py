import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.cuentas.services import CuentaService


class CuentaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.cuentas.listar_cuenta"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Cuentas"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("cuentas:create")
        context["listApiUrl"] = reverse_lazy("api_cuentas:list")
        context["updateUrl"] = reverse_lazy("cuentas:update", args=[0])
        context["deleteUrl"] = reverse_lazy("cuentas:delete", args=[0])
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
                "data": "banco",
                "name": "banco",
                "title": "Banco",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "tipo",
                "name": "tipo",
                "title": "Tipo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "pago_movil",
                "name": "pago_movil",
                "title": "Pago Móvil",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "telefono",
                "name": "telefono",
                "title": "Teléfono",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "empleado",
                "name": "empleado",
                "title": "Empleado",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class CuentaListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.cuentas.listar_cuenta"

    def __init__(self):
        self.service = CuentaService()
