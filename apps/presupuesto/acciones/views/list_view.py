import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import AccionService


class AccionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Acciones"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("acciones:create")
        context["listApiUrl"] = reverse_lazy("api_acciones:list")
        context["updateUrl"] = reverse_lazy("acciones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("acciones:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_acciones:export_pdf")
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
                "data": "nombrep",
                "name": "nombrep",
                "title": "Nombre",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fechai",
                "name": "fechai",
                "title": "Inicio",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fechac",
                "name": "fechac",
                "title": "Culminación",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "situacionp",
                "name": "situacionp",
                "title": "Situación Presupuestaria",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "montoproyecto",
                "name": "montoproyecto",
                "title": "Monto Total del Proyecto",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsableg",
                "name": "responsableg",
                "title": "Gerente Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsablet",
                "name": "responsablet",
                "title": "Técnico Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsabler",
                "name": "responsabler",
                "title": "Registrador Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsablea",
                "name": "responsablea",
                "title": "Responsable Administrativo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class AccionListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = AccionService()
