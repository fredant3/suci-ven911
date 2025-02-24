import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.familiares.services import FamiliarService


# parentezco
# tipo_hijo
# discapacidad
# nombres
# apellidos
# cedula
# fecha_nacimiento
# sexo
# estado_civil
# empleado__nombres
# observacion
class FamiliarListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.familiares.listar_familiar"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Familiar"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("familiares:create")
        context["listApiUrl"] = reverse_lazy("api_familiares:list")
        context["updateUrl"] = reverse_lazy("familiares:update", args=[0])
        context["deleteUrl"] = reverse_lazy("familiares:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "parentezco",
                "name": "parentezco",
                "title": "Parentesco",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "tipo_hijo",
                "name": "tipo_hijo",
                "title": "Tipo de hijo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "discapacidad",
                "name": "discapacidad",
                "title": "Discapacidad",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "nombres",
                "name": "nombres",
                "title": "Nombres",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "apellidos",
                "name": "apellidos",
                "title": "Apellidos",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cédula",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha_nacimiento",
                "name": "fecha_nacimiento",
                "title": "Fecha de nacimiento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "sexo",
                "name": "sexo",
                "title": "Sexo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estado_civil",
                "name": "estado_civil",
                "title": "Estado civil",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "empleado__nombres",
                "name": "empleado__nombres",
                "title": "Empleado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "observacion",
                "name": "observacion",
                "title": "Observaciones",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class FamiliarListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.familiares.editar_familiar"

    def __init__(self):
        self.service = FamiliarService()
