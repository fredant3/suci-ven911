from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from gestion_comunicacional.social_activity.services.SocialActivityService import (
    SocialActivityService,
)


class ListSocialActivity(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def get(self, request):
        page = request.GET.get("page") or 1
        search = None

        if "search" in request.GET:
            search = request.GET["search"]

        entities = self.service.getAll(page, search)

        return render(request, self.template_name, {"entities": entities})


class CreateSocialActivity(LoginRequiredMixin, CreateView):
    login_url = "login"
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def post(self, request):
        entity = self.service.creator(request.POST)

        return render(request, self.template_name, {"entity": entity})


class ReadSocialActivity(LoginRequiredMixin, DetailView):
    login_url = "login"
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def get(self, request, pk):
        entity = self.service.getById(pk)

        if not entity:
            return HttpResponse(status=404)

        return render(request, self.template_name, {"entity": entity})


class UpdateSocialActivity(LoginRequiredMixin, UpdateView):
    login_url = "login"
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def post(self, request, pk):
        entity = self.service.updater(request.PUT, pk)

        return render(request, self.template_name, {"entity": entity})


class DeleteSocialActivity(LoginRequiredMixin, DeleteView):
    login_url = "login"
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def post(self, request, pk):
        entity = self.service.destroyer(pk)

        return render(request, self.template_name, {"entity": entity})
