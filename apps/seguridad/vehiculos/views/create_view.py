from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import VehiculoForm
from ..services import VehiculoService


class VehiculoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = VehiculoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Vehiculos"
        context["titleForm"] = "Añadir una vehiculo nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("vehiculos:list")
        context["urlForm"] = reverse_lazy("api_vehiculos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class VehiculoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = VehiculoForm

    def __init__(self):
        self.service = VehiculoService()
