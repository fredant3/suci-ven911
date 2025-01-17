import json

from administracion.departamentos.services import DepartamentoService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class DepartamentoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administracion"
        context["submodule"] = "Departamento"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("departamentos:create")
        context["listApiUrl"] = reverse_lazy("api_departamentos:list")
        context["updateUrl"] = reverse_lazy("departamentos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("departamentos:delete", args=[0])
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
                "data": "nombre",
                "name": "nombre",
                "title": "Nombre",
                "orderable": "true",
                "searchable": "true",
            },
        ]


class DepartamentoListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = DepartamentoService()
