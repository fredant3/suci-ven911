import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from gestion_comunicacional.frente_preventivo.services import FrentePreventivoService


class FrentePreventivoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "frentepreventivo.ver_frentepreventivo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Frente Preventivo"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Frente Preventivo"
        context["submodule"] = "Inicio"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("frentepreventivo:create")
        context["listApiUrl"] = reverse_lazy("api_frentepreventivo:list")
        context["updateUrl"] = reverse_lazy("frentepreventivo:update", args=[0])
        context["deleteUrl"] = reverse_lazy("frentepreventivo:delete", args=[0])
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
                "data": "donde_desarrollo",
                "name": "donde_desarrollo",
                "title": "Donde se desarrollo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "personas_beneficiadas",
                "name": "personas_beneficiadas",
                "title": "Personas beneficiadas",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "tipo_actividad",
                "name": "tipo_actividad",
                "title": "Tipo de actividad",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class FrentePreventivoListApiView(ListController, CheckPermisosMixin):
    permission_required = "frentepreventivo.ver_frentepreventivo"

    def __init__(self):
        self.service = FrentePreventivoService()
