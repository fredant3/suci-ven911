# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from gestion_comunicacional.social_media.services.SocialMediaAccountService import (
    SocialMediaAccountService,
)


class SocialMediaAccountController:
    def __init__(self):
        self.service = SocialMediaAccountService()

    # @login_required(login_url="login")
    def listing(self, request):
        page = request.GET.get("page") or 1
        search = None

        if "search" in request.GET:
            search = request.GET["search"]

        entities = self.service.getAll(page, search)

        return render(request, "gc/social-media-account.html", {"data": entities})

    # @login_required(login_url="login")
    def create(self, request):
        if request.method not in ["POST"]:
            raise HttpResponseNotAllowed(["POST"])

        entity = self.service.creator(request.POST)

        return render(request, "gc/social-media-account.html", entity)

    # @login_required(login_url="login")
    def read(self, request, id):
        if request.method not in ["GET"]:
            raise HttpResponseNotAllowed(["GET"])

        entity = self.service.getById(id)

        if not entity:
            return HttpResponse(status=404)

        return render(request, "gc/social-media-account.html", entity)

    # @login_required(login_url="login")
    def update(self, request, id):
        if request.method not in ["PUT"]:
            raise HttpResponseNotAllowed(["PUT"])

        entity = self.service.updater(request.PUT, id)

        return render(request, "gc/social-media-account.html", entity)

    # @login_required(login_url="login")
    def delete(self, request, id):
        if request.method not in ["DELETE"]:
            raise HttpResponseNotAllowed(["DELETE"])

        entity = self.service.destroyer(id)

        return render(request, "gc/social-media-account", entity)
