from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from organizacion.normativas.forms import NormativaForm
from organizacion.normativas.services import NormativaService
from templates.sneat import TemplateLayout
from django.http import JsonResponse

class NormativaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = NormativaForm
    template_name = "sneat/layout/partials/form/layout_normativas.html"
    success_url = reverse_lazy("normativas:list") 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organización"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organización"
        context["submodule"] = "Normativas"
        context["titleForm"] = "Añadir una normativa"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("normativas:list")
        context["urlForm"] = reverse_lazy("api_normativas:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return JsonResponse({"message": "Se ha registrado con éxito."})

class NormativaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = NormativaForm

    def __init__(self):
        self.service = NormativaService()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Se ha registrado con éxito."})
        else:
            return self.form_invalid(form)
