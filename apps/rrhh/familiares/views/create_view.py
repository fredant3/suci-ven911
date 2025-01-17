from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import FamiliarForm
from ..services import FamiliarService


class FamiliarCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = FamiliarForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Familiars"
        context["titleForm"] = "Añadir una familiar nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("familiares:list")
        context["urlForm"] = reverse_lazy("api_familiares:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class FamiliarCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = FamiliarForm

    def __init__(self):
        self.service = FamiliarService()
