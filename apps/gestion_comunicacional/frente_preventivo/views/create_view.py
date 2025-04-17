from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from gestion_comunicacional.frente_preventivo.forms import FrentePreventivoForm
from gestion_comunicacional.frente_preventivo.forms import FrentepreventivoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout


class FrentepreventivoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "frentepreventivo.agregar_frentepreventivo"
    form_class = FrentePreventivoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Frente Preventivo"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Frente Preventivo"
        context["submodule"] = "Frente Preventivo"
        context["titleForm"] = "Añadir una Actividad"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("FrentePreventivo:list")
        context["urlForm"] = reverse_lazy("api_FrentePreventivo:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class FrentepreventivoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "frentepreventivo.agregar_frentepreventivo"
    form_class = FrentePreventivoForm

    def __init__(self):
        self.service = FrentepreventivoService()
