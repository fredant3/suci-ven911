from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import RegistroFilmicoForm
from ..services import RegistroFilmicoService


class RegistroFilmicoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = RegistroFilmicoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Registro Filmico"
        context["titleForm"] = "Añadir un registro filmico"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("filmicos:list")
        context["urlForm"] = reverse_lazy("api_filmicos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class RegistroFilmicoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = RegistroFilmicoForm

    def __init__(self):
        self.service = RegistroFilmicoService()
