from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class InfoController(LoginRequiredMixin, TemplateView):
    login_url = "login"
    template_name = "gc/index.html"
