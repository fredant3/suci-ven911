from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from rrhh.cuentas.forms import CuentaForm
from rrhh.cuentas.models import Cuenta
from rrhh.cuentas.services import CuentaService


class CuentaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "rrhh.cuentas.editar_cuenta"
    form_class = CuentaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Cuentas"
        context["titleForm"] = "Actualizar cuenta"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("cuentas:list")
        context["urlForm"] = reverse_lazy(
            "api_cuentas:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Cuenta.objects.filter(pk=id)


class CuentaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "rrhh.cuentas.editar_cuenta"
    form_class = CuentaForm

    def __init__(self):
        self.service = CuentaService()
