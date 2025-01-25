from administracion.compras.forms import CompraForm
from administracion.compras.model import Compra
from administracion.compras.services import CompraService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class CompraDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administrasion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Administrasion"
        context["submodule"] = "compra"
        context["titleForm"] = "Eliminar Compra"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("compra:list")
        context["urlDelete"] = reverse_lazy(
            "api_compra:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Compra.objects.filter(pk=id)


class CompraDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = CompraForm

    def __init__(self):
        self.service = CompraService()
