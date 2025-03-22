import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import UserService


class UserListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "user.ver_users"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Users"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Users"
        context["submodule"] = "Inicio"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("user:create")
        context["listApiUrl"] = reverse_lazy("api_user:list")
        context["updateUrl"] = reverse_lazy("user:update", args=[0])
        context["deleteUrl"] = reverse_lazy("user:delete", args=[0])
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
                "data": "username",
                "name": "username",
                "title": "Usuario",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "dni",
                "name": "dni",
                "title": "Cédula de Iden.",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "is_active",
                "name": "is_active",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class UserListApiView(ListController, CheckPermisosMixin):
    permission_required = "user.ver_users"

    def __init__(self):
        self.service = UserService()
