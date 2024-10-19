from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import DotacionForm
from ..models import Dotacion
from ..services import DotacionService


class DotacionUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = DotacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Dotacions"
        context["titleForm"] = "Actualizar dotacion"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("dotaciones:list")
        context["urlForm"] = reverse_lazy(
            "api_dotaciones:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Dotacion.objects.filter(pk=id)


class DotacionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = DotacionForm

    def __init__(self):
        self.service = DotacionService()
