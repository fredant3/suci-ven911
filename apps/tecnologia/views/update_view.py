from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from tecnologia.forms import TecnologiaForm
from tecnologia.services import TecnologiaService
from templates.sneat import TemplateLayout


class TecnologiaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = TecnologiaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnologia de la Informacion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Tecnologia de la Informacion"
        context["submodule"] = "Tecnologia"
        context["titleForm"] = "Actualizar registro"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("tecnologia:list")
        context["urlForm"] = reverse_lazy(
            "api_tecnologia:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)



class TecnologiaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = TecnologiaForm

    def __init__(self):
        self.service = TecnologiaService()
