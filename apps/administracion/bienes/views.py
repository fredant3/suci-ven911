from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from templates.sneat import TemplateLayout


class Modules(LoginRequiredMixin, TemplateView):
    # form_class = SocialMediaAccountForm
    template_name = "administracion/bienes/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Bienes"
        context["indexModuleUrl"] = reverse_lazy("gc:info")
        context["module"] = "Bienes"
        context["submodule"] = "Bienes - s"
        context["titleForm"] = "gc_sm_account_title_form"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("modules:index")
        context["urlForm"] = reverse_lazy("modules:index")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)
