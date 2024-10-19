from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import CargoForm
from ..models import Cargo
from ..services import CargoService


class CargoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = CargoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Cargos"
        context["titleForm"] = "Actualizar cargo"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("cargos:list")
        context["urlForm"] = reverse_lazy(
            "api_cargos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Cargo.objects.filter(pk=id)


class CargoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = CargoForm

    def __init__(self):
        self.service = CargoService()
