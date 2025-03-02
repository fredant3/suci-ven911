import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.empleados.services import EmpleadoService


class EmpleadoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.empleados.listar_empleado"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Empleados"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("empleados:create")
        context["listApiUrl"] = reverse_lazy("api_empleados:list")
        context["updateUrl"] = reverse_lazy("empleados:update", args=[0])
        context["deleteUrl"] = reverse_lazy("empleados:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_empleados:export_excel")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "nombres",
                "name": "nombres",
                "title": "Nombres",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "apellidos",
                "name": "apellidos",
                "title": "Apellidos",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cedula",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "fecha_nacimiento",
                "name": "fecha_nacimiento",
                "title": "Fecha Nacimiento",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "email",
                "name": "email",
                "title": "Email",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "telefono",
                "name": "telefono",
                "title": "Telefono",
                "orderable": "true",
                "searchable": "true",
            },
        ]


class EmpleadoListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.empleados.listar_empleado"

    def __init__(self):
        self.service = EmpleadoService()
