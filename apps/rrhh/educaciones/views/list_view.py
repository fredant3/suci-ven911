import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.educaciones.services import EducacionService


class EducacionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.educacion.listar_educacion"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Educacion"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("educaciones:create")
        context["listApiUrl"] = reverse_lazy("api_educaciones:list")
        context["updateUrl"] = reverse_lazy("educaciones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("educaciones:delete", args=[0])
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
                "data": "colegio",
                "name": "colegio",
                "title": "Colegio",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "codigo_titulo",
                "name": "codigo_titulo",
                "title": "Código ",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "area_conocimiento",
                "name": "area_conocimiento",
                "title": "Área de Conocimiento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "empleado",
                "name": "empleado",
                "title": "Empleado",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class EducacionListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.educacion.listar_educacion"

    def __init__(self):
        self.service = EducacionService()
