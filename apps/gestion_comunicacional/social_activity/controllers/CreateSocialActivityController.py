from gestion_comunicacional.social_activity.forms.SocialActivityForm import SocialActivityForm
from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService
from index.mixins.ControllerMixin import CreateController
from templates.sneat import TemplateLayout

from django.urls import reverse_lazy


class CreateSocialActivity(CreateController):
    template_name = "gc/social-activity/create.html"
    form_class = SocialActivityForm

    def __init__(self):
        self.service = SocialActivityService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sa_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sa_module_name"
        context["titleForm"] = "gc_sa_title_form"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gc:sa:listing-activity")
        context["urlForm"] = reverse_lazy("gc:sa:create-activity")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)
