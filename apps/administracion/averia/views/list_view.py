import json

from administracion.averia.services import AveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class AveriaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administracion"
        context["submodule"] = "Averia"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("averias:create")
        context["listApiUrl"] = reverse_lazy("api_averias:list")
        context["updateUrl"] = reverse_lazy("averias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("averias:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "#",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "problema",
                "name": "problema",
                "title": "Problema",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "tipo_averia",
                "name": "tipo_averia",
                "title": "Tipo de avería",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "departamento",
                "name": "departamento",
                "title": "Departamento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "ubicacion",
                "name": "ubicacion",
                "title": "Ubicación",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "serial",
                "name": "serial",
                "title": "Serial",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "codigo_bn",
                "name": "codigo_bn",
                "title": "Código BN",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "user",
                "name": "creadopor",
                "title": "Creado por",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class AveriaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = AveriaService()
