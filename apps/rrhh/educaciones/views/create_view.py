from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import EducacionForm
from ..services import EducacionService


class EducacionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = EducacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Educacions"
        context["titleForm"] = "Añadir una educacion nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("educaciones:list")
        context["urlForm"] = reverse_lazy("api_educaciones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class EducacionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = EducacionForm

    def __init__(self):
        self.service = EducacionService()
