import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout
from helpers.ControllerMixin import ListController
from organizacion.services import OrganizacionService
from organizacion.normativas.models import Normativa
from organizacion.reglamentos.models import Reglamento


class OrganizacionView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "organizacion_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/layout_module.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizaciones"
        context["module"] = "Organizacion"
        context["listApiUrl"] = reverse_lazy("api_organizacion")
        context["withActions"] = False
        context["cards"] = self.getCards()
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getCards(self):
        return [
            {
                "title": "Archivos de tipos",
                "subtitle": "Normativas",
                "href": reverse_lazy("normativas:list"),
                "body": [
                    {
                        "title": "Activos",
                        "info": "Normativas para biblioteca",
                        "detail": Normativa.objects.filter(estado=True).count(),
                    },
                    {
                        "title": "Archivos de tipo",
                        "info": "Normativas para uso interno",
                        "detail": Normativa.objects.all().count(),
                    },
                ],
            },
            {
                "title": "Archivos de tipos",
                "subtitle": "Reglamentos",
                "href": reverse_lazy("reglamentos:list"),
                "body": [
                    {
                        "title": "Activos",
                        "info": "Reglamentos para biblioteca",
                        "detail": Reglamento.objects.filter(estado=True).count(),
                    },
                    {
                        "title": "Total de archivos",
                        "info": "Reglamentos para uso interno",
                        "detail": Reglamento.objects.all().count(),
                    },
                ],
            },
        ]

    def getColumns(self):
        return [
            {
                "data": "name",
                "name": "name",
                "title": "Nombre del Archivo",
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
                "data": "estado",
                "name": "estado",
                "title": "Estado",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class OrganizacionApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = OrganizacionService()
