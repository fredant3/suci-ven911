from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import CuadrantePazForm
from ..services import CuadrantePazService


class CuadrantePazCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = CuadrantePazForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Cuadrantes de Paz"
        context["titleForm"] = "Añadir una cuadrante de paz nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("cuadrantes_paz:list")
        context["urlForm"] = reverse_lazy("api_cuadrantes_paz:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class CuadrantePazCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = CuadrantePazForm

    def __init__(self):
        self.service = CuadrantePazService()
