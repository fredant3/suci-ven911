import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import EmergenciaService


class EmergenciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Emergencias"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Emergencias"
        context["submodule"] = "Inicio"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("emergencias:create")
        context["listApiUrl"] = reverse_lazy("api_emergencias:list")
        context["updateUrl"] = reverse_lazy("emergencias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("emergencias:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "Denunciante",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "denunciante",
                "name": "estatus",
                "title": "Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "telefono_denunciante",
                "name": "nombres_d",
                "title": "Telefono",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "datecompleted",
                "name": "apellidos_d",
                "title": "Completado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "created_by",
                "name": "cedula_d",
                "title": "Creado por",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class EmergenciaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = EmergenciaService()
