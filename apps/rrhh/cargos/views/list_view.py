import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.cargos.services import CargoService


class CargoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.cargos.listar_cargo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion Humana"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Cargos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("cargos:create")
        context["listApiUrl"] = reverse_lazy("api_cargos:list")
        context["updateUrl"] = reverse_lazy("cargos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("cargos:delete", args=[0])
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
                "data": "cargo",
                "name": "cargo",
                "title": "Cargo",
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


class CargoListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.cargos.listar_cargo"

    def __init__(self):
        self.service = CargoService()
