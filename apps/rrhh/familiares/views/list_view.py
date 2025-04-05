import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.familiares.services import FamiliarService
from helpers.models import BOOLEAN_CHOICES, ESTADO_CIVIL_CHOICES, SEXO_CHOICES
from rrhh.familiares.models import PARENTEZCO, TIPO_HIJO


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
        context["exportExcelUrl"] = reverse_lazy("api_familiares:export_excel")
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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if response.status_code == 200 and response.content:
            try:
                data = json.loads(response.content)

                # Mapeos para los campos con choices
                parentezco_map = dict(PARENTEZCO)
                tipo_hijo_map = dict(TIPO_HIJO)
                discapacidad_map = dict(BOOLEAN_CHOICES)
                sexo_map = dict(SEXO_CHOICES)
                estado_civil_map = dict(ESTADO_CIVIL_CHOICES)

                for item in data.get("entities", []):
                    # Convertir parentezco
                    if "parentezco" in item:
                        item["parentezco"] = parentezco_map.get(
                            item["parentezco"], item["parentezco"]
                        )

                    # Convertir tipo_hijo
                    if "tipo_hijo" in item and item["tipo_hijo"]:
                        item["tipo_hijo"] = tipo_hijo_map.get(
                            item["tipo_hijo"], item["tipo_hijo"]
                        )

                    # Convertir discapacidad
                    if "discapacidad" in item:
                        discapacidad_value = item["discapacidad"]
                        if isinstance(discapacidad_value, bool):
                            item["discapacidad"] = discapacidad_map.get(
                                discapacidad_value, str(discapacidad_value)
                            )
                        else:
                            item["discapacidad"] = "Sí" if discapacidad_value else "No"

                    # Convertir sexo
                    if "sexo" in item:
                        item["sexo"] = sexo_map.get(item["sexo"], item["sexo"])

                    # Convertir estado_civil
                    if "estado_civil" in item:
                        item["estado_civil"] = estado_civil_map.get(
                            item["estado_civil"], item["estado_civil"]
                        )

                    # Formatear fecha
                    if "fecha_nacimiento" in item and item["fecha_nacimiento"]:
                        item["fecha_nacimiento"] = item["fecha_nacimiento"][
                            :10
                        ]  # Solo fecha sin hora

                response.content = json.dumps(data)
            except json.JSONDecodeError as e:
                print(f"Error decodificando JSON: {e}")
        return response
