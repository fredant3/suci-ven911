import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


from organizacion.normativas.services import NormativaService


class NormativaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "biblioteca/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Biblioteca"
        context["module"] = "Biblioteca"
        context["submodule"] = "Normativas"
        context["submodules"] = json.dumps(
            (
                {
                    "api": "{0}?length=3&order[0][name]=date&order[0][dir]=desc&search[value]=(estado=1)".format(
                        str(reverse_lazy("api_biblioteca_normativas:list"))
                    ),
                    # "api": "",
                    "name": "Normativas",
                },
            )
        )
        return TemplateLayout.init(self, context)


class NormativaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = NormativaService()
