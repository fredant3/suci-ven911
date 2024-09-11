from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from templates.sneat import TemplateLayout
from templates.sneat.helpers.theme import TemplateHelper
from users.authentication.forms.LoginForm import LoginForm


class LoginController(LoginView):
    form_class = LoginForm
    next_page = reverse_lazy("index:modules:module")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["uri_api_login"] = "users:auth:api_login"
        context.update(
            {"layout_path": TemplateHelper.set_layout("layout_blank.html", context)}
        )
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginController, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
