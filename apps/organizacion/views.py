import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class OrganizacionView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/layout_module.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizaciones"
        context["module"] = "Organizacion"
        context["listApiUrl"] = reverse_lazy("api_reglamentos:list")
        context["cards"] = self.getCards()
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getCards(self):
        return [
            {
                "title": "Total de Informes",
                "subtitle": "Tipo de Informe",
                "info": "Normativas",
                "detail": "32",
                "href": reverse_lazy("normativas:list"),
            },
            {
                "title": "Total de Informes",
                "subtitle": "Tipo de Informe",
                "info": "Reglamentos",
                "detail": "32",
                "href": reverse_lazy("reglamentos:list"),
            },
        ]

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
                "data": "file",
                "name": "file",
                "title": "Archivo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "user",
                "name": "user",
                "title": "Usuario",
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
