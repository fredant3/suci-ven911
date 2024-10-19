from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import CuadrantePazForm
from ..models import CuadrantePaz
from ..services import CuadrantePazService


class CuadrantePazUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = CuadrantePazForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Cuadrantes de Paz"
        context["titleForm"] = "Actualizar cuadrante de paz"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("cuadrantes_paz:list")
        context["urlForm"] = reverse_lazy(
            "api_cuadrantes_paz:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return CuadrantePaz.objects.filter(pk=id)


class CuadrantePazUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = CuadrantePazForm

    def __init__(self):
        self.service = CuadrantePazService()
