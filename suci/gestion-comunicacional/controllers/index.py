from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import SocialMediaAccount
from .forms import CreateSocialMediaAccount, UpdateSocialMediaAccount


@login_required(login_url="login")
def info(request):
    return render(request, "gc/index.html")
