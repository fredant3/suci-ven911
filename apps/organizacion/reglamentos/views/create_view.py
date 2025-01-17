from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from organizacion.reglamentos.forms import ReglamentoForm
from organizacion.reglamentos.services import ReglamentoService
from templates.sneat import TemplateLayout
from django.http import JsonResponse

class ReglamentoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = ReglamentoForm
    template_name = "sneat/layout/partials/form/layout_normativas.html"
    success_url = reverse_lazy("reglamentos:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organización"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organización"
        context["submodule"] = "Reglamentos"
        context["titleForm"] = "Añadir un reglamento"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("reglamentos:list")
        context["urlForm"] = reverse_lazy("api_reglamentos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return JsonResponse({"message": "Se ha registrado con éxito."})

class ReglamentoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ReglamentoForm

    def __init__(self):
        self.service = ReglamentoService()
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Se ha registrado con éxito."})
        else:
            return self.form_invalid(form)