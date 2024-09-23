import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class BibliotecatView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "biblioteca/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Biblioteca"
        context["module"] = "Biblioteca"
        context["submodules"] = json.dumps(
            (
                {
                    "url": str(reverse_lazy("normativas:list")),
                    "api": str(reverse_lazy("api_normativas:list")),
                    "name": "Normativas",
                },
                {
                    "url": str(reverse_lazy("reglamentos:list")),
                    "api": str(reverse_lazy("api_reglamentos:list")),
                    "name": "Reglamentos",
                },
            )
        )
        return TemplateLayout.init(self, context)
