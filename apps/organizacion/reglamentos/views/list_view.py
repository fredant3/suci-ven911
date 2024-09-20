import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import ReglamentoService


class ReglamentoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Organizacion"
        context["submodule"] = "Reglamentos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("reglamentos:create")
        context["listApiUrl"] = reverse_lazy("api_reglamentos:list")
        context["updateUrl"] = reverse_lazy("reglamentos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("reglamentos:delete", args=[0])
        # context["exportExcelUrl"] = reverse_lazy("api_reglamentos:export_excel")
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
                "data": "name",
                "name": "name",
                "title": "Nombre de Reglamento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "file",
                "name": "file",
                "title": "Archivo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "user",
                "name": "user",
                "title": "Usuario",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "date",
                "name": "date",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "progre",
                "name": "progre",
                "title": "Progreso",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estado",
                "name": "estado",
                "title": "Estado",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class ReglamentoListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = ReglamentoService()
