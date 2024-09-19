import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import DenunciaService


class DenunciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("denuncias:create")
        context["listApiUrl"] = reverse_lazy("api_denuncias:list")
        context["updateUrl"] = reverse_lazy("denuncias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("denuncias:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_denuncias:export_excel")
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
                "title": "Nombre del Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "apellidos_d",
                "name": "apellidos_d",
                "title": "Apellido del Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cedula_d",
                "name": "cedula_d",
                "title": "Cédula del Denunciante",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "fecha_denuncia",
                "name": "fecha_denuncia",
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


class DenunciaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = DenunciaService()
