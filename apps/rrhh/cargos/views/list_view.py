import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.cargos.services import CargoService
from rrhh.cargos.models import ESTATUS_CHOICES


class CargoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.cargos.listar_cargo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Cargos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("cargos:create")
        context["listApiUrl"] = reverse_lazy("api_cargos:list")
        context["updateUrl"] = reverse_lazy("cargos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("cargos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_cargos:export_excel")
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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if response.status_code == 200 and response.content:
            try:
                data = json.loads(response.content)
                estatus_mapping = dict(ESTATUS_CHOICES)

                # Convertir estatus a su valor legible
                for item in data.get("entities", []):
                    if "estatus" in item:
                        item["estatus"] = estatus_mapping.get(
                            item["estatus"], item["estatus"]
                        )

                response.content = json.dumps(data)
            except json.JSONDecodeError as e:
                print(f"Error decodificando JSON: {e}")
        return response
