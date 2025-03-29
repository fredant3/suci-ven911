from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService
from index.mixins.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView


class ListSocialMediaAccount(LoginRequiredMixin, ListView):
    # class ListSocialMediaAccount(LoginRequiredMixin, CheckPermisosMixin, ListView):
    # permission_required = "session.change_session"
    url_redirect = reverse_lazy("gc:info")
    template_name = "gc/social-media/accounts/listing.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sm_account_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sm_module_name"
        context["createBtn"] = "gc_sm_account_title_btn_add"
        context["createUrl"] = reverse_lazy("gc:sm:create-account")
        context["listUrl"] = reverse_lazy("gc:sm:listing-account")
        context["updateUrl"] = reverse_lazy("gc:sm:updater-account", args=[0])
        context["deleteUrl"] = reverse_lazy("gc:sm:destroyer-account", args=[0])
        context["columns"] = "id|platform|username_sm|followers|responsible|publications"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        # self.kwargs['page']
        page = self.request.GET.get("page") or 1
        search = self.request.GET.get("search") or None

        return self.service.getAll(page, search)

    def get(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            data = {}
            try:
                data = self.get_queryset()
            except Exception as e:
                data["error"] = str(e)
            return JsonResponse(data, safe=False)

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
