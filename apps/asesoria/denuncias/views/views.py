import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import (
    CreateController,
    DeleteController,
    ListController,
    UpdateController,
)

from templates.sneat import TemplateLayout

from ..forms import DenunciaForm
from ..services import DenunciaService


class DenunciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("denuncias:create")
        context["listApiUrl"] = reverse_lazy("api_denuncias:list")
        context["updateUrl"] = reverse_lazy("denuncias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("denuncias:delete", args=[0])
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
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "nombres_d",
                "name": "nombres_d",
                "title": "Nombre del Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "apellidos_d",
                "name": "apellidos_d",
                "title": "Apellido del Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cedula_d",
                "name": "cedula_d",
                "title": "Cédula del Denunciante",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "fecha_denuncia",
                "name": "fecha_denuncia",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "telefono",
                "name": "telefono",
                "title": "Teléfono",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "email",
                "name": "email",
                "title": "Correo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "motivo",
                "name": "motivo",
                "title": "Motivo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "title": "Acciones",
            },
        ]


class DenunciaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = DenunciaService()


class DenunciaCreateApiView(CreateController):
    form_class = DenunciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["titleForm"] = "Añadir una denuncia nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("denuncias:list")
        context["urlForm"] = reverse_lazy("api_denuncias:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        # self.kwargs['page']
        page = self.request.GET.get("page") or 1
        search = self.request.GET.get("search") or None

        return self.service.getAll(page, search)

    def get(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            data = {}
            try:
                data = self.get_queryset()
            except Exception as e:
                data["error"] = str(e)
            return JsonResponse(data, safe=False)

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class UpdateSocialMediaAccount(UpdateController):
    form_class = DenunciaForm
    template_name = "gc/social-media/accounts/update.html"
    redirect_not_found = reverse_lazy("gc:sm:listing-account")

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sm_account_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sm_module_name"
        context["titleForm"] = "gc_sm_account_title_form"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gc:sm:listing-account")
        context["urlForm"] = reverse_lazy(
            "gc:sm:updater-account", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)


class DeleteSocialMediaAccount(DeleteController):
    template_name = "gc/social-media/accounts/delete.html"
    redirect_not_found = reverse_lazy("gc:sm:listing-account")

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sm_account_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sm_module_name"
        context["titleForm"] = "gc_sm_account_title_form"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("gc:sm:listing-account")
        context["urlDelete"] = reverse_lazy(
            "gc:sm:destroyer-account", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)
