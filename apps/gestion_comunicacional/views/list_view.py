import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from gestion_comunicacional.services import GestioncomunicacionalService


class EmergenciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "gestioncomuicacional.ver_gestioncomunicacional"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion comunicacional"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Gestion comunicacional"
        context["submodule"] = "Inicio"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("gestioncomunicacional:create")
        context["listApiUrl"] = reverse_lazy("api_gestioncomunicacional:list")
        context["updateUrl"] = reverse_lazy("gestioncomunicacional:update", args=[0])
        context["deleteUrl"] = reverse_lazy("gestioncomunicacional:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("gestioncomunicacional:export_excel")
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
                "searchable": "true",
            },
            {
                "data": "denunciante",
                "name": "denunciante",
                "title": "Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "telefono_denunciante",
                "name": "telefono_denunciante",
                "title": "Telefono",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "created_by",
                "name": "created_by",
                "title": "Creado por",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class EmergenciaListApiView(ListController, CheckPermisosMixin):
    permission_required = "gestioncomunicacional.ver_gestioncomunicacional"

    def __init__(self):
        self.service = GestioncomunicacionalService()
