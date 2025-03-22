from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tecnologia.usuarios.forms import UserForm

from tecnologia.usuarios.services import UserService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class UserCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = UserForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Users"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Users"
        context["submodule"] = "Users"
        context["titleForm"] = "Añadir una Usuario"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("user:list")
        context["urlForm"] = reverse_lazy("api_user:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class UserCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "user.agregar_user"
    form_class = UserForm

    def __init__(self):
        self.service = UserService()
