from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from templates.sneat import TemplateLayout
from templates.sneat.helpers.theme import TemplateHelper


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("index:auth:login")


class AuthView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update({"layout_path": TemplateHelper.set_layout("layout_blank.html", context)})
        return context
