import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from rrhh.dotaciones.services import DotacionService


class DotacionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.dotaciones.listar_dotacion"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Dotaciones"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("dotaciones:create")
        context["listApiUrl"] = reverse_lazy("api_dotaciones:list")
        context["updateUrl"] = reverse_lazy("dotaciones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("dotaciones:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "camisa",
                "name": "camisa",
                "title": "Camisa",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "pantalon",
                "name": "pantalon",
                "title": "Pantalon",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cedula",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "zapato",
                "name": "zapato",
                "title": "Zapato",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "empleado___nombres",
                "name": "empleado___nombres",
                "title": "Empleado",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class DotacionListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.dotaciones.listar_dotacion"

    def __init__(self):
        self.service = DotacionService()
