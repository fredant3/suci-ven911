import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.tipos_sueldos.services import TipoSueldoService
from rrhh.tipos_sueldos.models import ESTATUS_CHOICES


class TipoSueldoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.tipos_sueldos.listar_tipo_sueldo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Tipos de Sueldos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("tipos_sueldos:create")
        context["listApiUrl"] = reverse_lazy("api_tipos_sueldos:list")
        context["updateUrl"] = reverse_lazy("tipos_sueldos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("tipos_sueldos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_tipos_sueldos:export_excel")
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
                "data": "tipo",
                "name": "tipo",
                "title": "Tipo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "monto",
                "name": "monto",
                "title": "Monto",
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


class TipoSueldoListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.tipos_sueldos.listar_tipo_sueldo"

    def __init__(self):
        self.service = TipoSueldoService()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if response.status_code == 200 and response.content:
            try:
                data = json.loads(response.content)
                estatus_mapping = dict(ESTATUS_CHOICES)

                # Convertir estatus y formatear monto
                for item in data.get("entities", []):
                    # Formatear estatus
                    if "estatus" in item:
                        item["estatus"] = estatus_mapping.get(
                            item["estatus"], item["estatus"]
                        )

                    # Formatear monto como número (opcional)
                    if "monto" in item:
                        try:
                            item["monto"] = float(item["monto"])
                        except (ValueError, TypeError):
                            item["monto"] = 0.0

                response.content = json.dumps(data)
            except json.JSONDecodeError as e:
                print(f"Error decodificando JSON: {e}")
        return response
