from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import SedeForm
from ..services import SedeService


class SedeCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = SedeForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administracion"
        context["submodule"] = "Sedes"
        context["titleForm"] = "Añadir una sede"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("sedes:list")
        context["urlForm"] = reverse_lazy("api_sedes:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class SedeCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = SedeForm

    def __init__(self):
        self.service = SedeService()
