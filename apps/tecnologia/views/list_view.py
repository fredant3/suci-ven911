import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from tecnologia.services import TecnologiaService

from templates.sneat import TemplateLayout


class TecnologiaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnologia de la Informacion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Tecnologia de la Informacion"
        context["submodule"] = "Tecnologia"
        context["createBtn"] = "Añadir"
        # context["createUrl"] = reverse_lazy("tecnologia:create")
        context["listApiUrl"] = reverse_lazy("api_tecnologia:list")
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
                "searchable": "false",
            },
            {
                "data": "marca",
                "name": "marca",
                "title": "Marca",
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
                "data": "fecha_adq",
                "name": "fecha_adq",
                "title": "Adquirido",
                "orderable": "false",
                "searchable": "false",
            },
        ]



class TecnologiaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = TecnologiaService()
