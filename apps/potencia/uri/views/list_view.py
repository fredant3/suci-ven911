import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from potencia.uri.services import UriService

from templates.sneat import TemplateLayout


class UriListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "potencia.uri.listar_uri"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("uri:create")
        context["listApiUrl"] = reverse_lazy("api_uri:list")
        context["updateUrl"] = reverse_lazy("uri:update", args=[0])
        context["deleteUrl"] = reverse_lazy("uri:delete", args=[0])
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
                "data": "nombre_apellido",
                "name": "nombre_apellido",
                "title": "Nombre completo",
                "orderable": "true",
                "searchable": "true",
            },
        ]


class UriListApiView(ListController, CheckPermisosMixin):
    permission_required = "potencia.uri.listar_uri"

    def __init__(self):
        self.service = UriService()
