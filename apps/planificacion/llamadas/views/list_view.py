import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import LlamadaService


class LlamadaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "planificacion.llamadas.listar_llamadas"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Llamadas"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("llamadas:create")
        context["listApiUrl"] = reverse_lazy("api_llamadas:list")
        context["updateUrl"] = reverse_lazy("llamadas:update", args=[0])
        context["deleteUrl"] = reverse_lazy("llamadas:delete", args=[0])
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
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "nombres_d",
                "name": "nombres_d",
                "title": "Nombre del Llamadante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "apellidos_d",
                "name": "apellidos_d",
                "title": "Apellido del Llamadante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cedula_d",
                "name": "cedula_d",
                "title": "Cédula del Llamadante",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "fecha_llamada",
                "name": "fecha_llamada",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "telefono",
                "name": "telefono",
                "title": "Teléfono",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "email",
                "name": "email",
                "title": "Correo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "motivo",
                "name": "motivo",
                "title": "Motivo",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class LlamadaListApiView(ListController, CheckPermisosMixin):
    permission_required = "planificacion.llamadas.listar_llamadas"

    def __init__(self):
        self.service = LlamadaService()
