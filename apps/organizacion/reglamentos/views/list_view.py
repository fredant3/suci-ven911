import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from organizacion.reglamentos.services import ReglamentoService
from organizacion.reglamentos.models import ESTATUS_CHOICES, PROGRESS_CHOICES


class ReglamentoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "organizacion.reglamentos.ver_reglamento"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Reglamentos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("reglamentos:create")
        context["listApiUrl"] = reverse_lazy("api_reglamentos:list")
        context["updateUrl"] = reverse_lazy("reglamentos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("reglamentos:delete", args=[0])
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
    permission_required = "organizacion.reglamentos.ver_reglamento"

    def __init__(self):
        self.service = ReglamentoService()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if response.status_code == 200 and response.content:
            try:
                data = json.loads(response.content)
                estatus_mapping = dict(ESTATUS_CHOICES)
                progress_mapping = dict(PROGRESS_CHOICES)

                for item in data.get("entities", []):
                    if "estado" in item:
                        item["estado"] = estatus_mapping.get(
                            item["estado"], item["estado"]
                        )

                    if "progre" in item:
                        item["progre"] = progress_mapping.get(
                            item["progre"], item["progre"]
                        )

                    if "date" in item and item["date"]:
                        item["date"] = (
                            item["date"][:10]
                            if isinstance(item["date"], str)
                            else item["date"].strftime("%Y-%m-%d")
                        )

                response.content = json.dumps(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
        return response
