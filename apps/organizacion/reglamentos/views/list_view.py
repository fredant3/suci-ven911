import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import ReglamentoService
from ..models import Reglamento

class ReglamentoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/reglamentos.html"

    def get_context_data(self, **kwargs):
        columns = Reglamento.objects.all()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organización"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organización"
        context["submodule"] = "Reglamentos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("reglamentos:create")
        context["listApiUrl"] = reverse_lazy("api_reglamentos:list")
        context["updateUrl"] = reverse_lazy("reglamentos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("reglamentos:delete", args=[0])
        context["heads"] = columns
        context["columns"] = columns
        return TemplateLayout.init(self, context)

class ReglamentoListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = ReglamentoService()
