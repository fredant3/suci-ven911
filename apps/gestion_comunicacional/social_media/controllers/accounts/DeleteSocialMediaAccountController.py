from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService
from index.mixins.ControllerMixin import DeleteController
from templates.sneat import TemplateLayout

from django.urls import reverse_lazy


class DeleteSocialMediaAccount(DeleteController):
    template_name = "gc/social-media/accounts/delete.html"
    redirect_not_found = reverse_lazy("gc:sm:listing-account")

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sm_account_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sm_module_name"
        context["titleForm"] = "gc_sm_account_title_form"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("gc:sm:listing-account")
        context["urlDelete"] = reverse_lazy("gc:sm:destroyer-account", args=[self.kwargs.get("pk")])
        return TemplateLayout.init(self, context)
