from administracion.inventario.forms import ArticuloForm
from administracion.inventario.models import Articulo
from administracion.inventario.services import InventarioService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class InventarioUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = ArticuloForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "administracion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Inventario"
        context["submodule"] = "Articulo"
        context["titleForm"] = "Actualizar"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("articulo:list")
        context["urlForm"] = reverse_lazy(
            "api_articulo:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Articulo.objects.filter(pk=id)


class ArticuloUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ArticuloForm

    def __init__(self):
        self.service = InventarioService()
