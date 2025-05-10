from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from presupuesto.traspaso.models import Traspaso
from presupuesto.traspaso.forms import TraspasoForm
from presupuesto.traspaso.services import TraspasoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class TraspasoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "presupuesto.traspaso.editar_traspaso"
    form_class = TraspasoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        context["titleForm"] = "Actualizar traspaso"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("traspasos:list")
        context["urlForm"] = reverse_lazy(
            "api_traspasos:update", kwargs={"pk": self.kwargs.get("pk")}
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Traspaso.objects.filter(pk=id)


class TraspasoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "presupuesto.traspaso.editar_traspaso"
    form_class = TraspasoForm

    def __init__(self):
        self.service = TraspasoService()
