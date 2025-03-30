from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from templates.sneat import TemplateLayout


class InfoController(LoginRequiredMixin, TemplateView):
    login_url = "auth:login"
    template_name = "gc/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
