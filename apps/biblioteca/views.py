import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class BibliotecatView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "biblioteca_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "biblioteca/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Biblioteca"
        context["module"] = "Biblioteca"
        context["submodules"] = json.dumps(
            (
                {
                    "url": str(reverse_lazy("biblioteca_normativas:list")),
                    "api": "{0}?length=3&order[0][name]=date&order[0][dir]=desc&search[0][estado]=1".format(
                        str(reverse_lazy("api_biblioteca_normativas:list"))
                    ),
                    # "api": "",
                    "name": "Normativas",
                },
                {
                    "url": str(reverse_lazy("biblioteca_reglamentos:list")),
                    "api": "{0}?length=3&order[0][name]=date&order[0][dir]=desc".format(
                        str(reverse_lazy("api_biblioteca_reglamentos:list"))
                    ),
                    # "api": "",
                    "name": "Reglamentos",
                },
            )
        )
        return TemplateLayout.init(self, context)
