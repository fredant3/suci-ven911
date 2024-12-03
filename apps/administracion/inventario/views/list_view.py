import json

from administracion.inventario.services import InventarioService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class ArticuloListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Inventario"
        context["submodule"] = "Artiulo"
        context["createUrl"] = reverse_lazy("articulos:create", args=[0])
        context["listApiUrl"] = reverse_lazy("api_articulos:list")
        context["updateUrl"] = reverse_lazy("articulos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("articulos:delete", args=[0])
        context["heads"] = columns
        context["isSelect"] = True
        context["selectTitle"] = "Añadir articulo"
        context["selectOptions"] = (
            ("tecnologia", "Tecnologia"),
            ("consumible", "Consumible"),
            ("mobiliario", "Mobiliario"),
            ("vehiculo", "Vehiculo"),
        )
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
                "data": "marca",
                "name": "marca",
                "title": "Tipo de Articulo",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "modelo",
                "name": "modelo",
                "title": "Modelo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "serial",
                "name": "serial",
                "title": "Serial",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cantidad_combustible",
                "name": "cantidad_combustible",
                "title": "Cantidad",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class ArticuloListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = InventarioService()
