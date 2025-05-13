from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from presupuesto.traspaso.forms import TraspasoForm
from presupuesto.traspaso.services import TraspasoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from presupuesto.cedente.forms import CedenteForm

from presupuesto.receptor.forms import ReceptorForm
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect


class TraspasoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "presupuesto.traspaso.agregar_traspaso"
    form_class = TraspasoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        context["titleForm"] = "Añadir una Traspaso"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("traspasos:list")
        context["urlForm"] = reverse_lazy("api_traspasos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class TraspasoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "presupuesto.traspaso.agregar_cedente"
    form_class = TraspasoForm

    def __init__(self):
        self.service = TraspasoService()


class TraspasoReceptorWizardView(
    LoginRequiredMixin, CheckPermisosMixin, SessionWizardView
):
    permission_required = "presupuesto.traspaso.agregar_cedente"
    template_name = "widzard/indextraspaso.html"
    form_list = [
        ("traspaso", TraspasoForm),
        ("cedente", CedenteForm),
        ("receptor", ReceptorForm),
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        return TemplateLayout.init(self, context)

    def done(self, form_list, form_dict, **kwargs):
        # Save Traspaso first
        traspaso = form_dict["traspaso"].save(commit=False)
        traspaso.created_by = self.request.user
        traspaso.save()

        # Save Cedente with the traspaso relationship
        cedente = form_dict["cedente"].save(commit=False)
        cedente.traspaso = traspaso
        cedente.created_by = self.request.user
        cedente.save()

        # Save Receptor with the traspaso relationship
        receptor = form_dict["receptor"].save(commit=False)
        receptor.traspaso = traspaso
        receptor.created_by = self.request.user
        receptor.save()

        return HttpResponseRedirect("/presupuesto/traspasos")
