from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import SocialMediaAccount
from .forms import CreateSocialMediaAccount, UpdateSocialMediaAccount


@login_required(login_url="login")
def listingSocialMediaAccount(request, accion=None):
    if accion is None:
        model = SocialMediaAccount.objects.all()

    elif accion == "consultar" and "search" in request.GET:
        search = request.GET["search"]
        model = SocialMediaAccount.objects.filter(username=search)

    else:
        model = SocialMediaAccount.objects.all()

    paginator = Paginator(model, 15)
    pagina = request.GET.get("page")

    try:
        currentPage = paginator.page(pagina)
    except PageNotAnInteger:
        currentPage = paginator.page(1)
    except EmptyPage:
        currentPage = Paginator.page(paginator.num_pages)

    context = {
        "createSocialMediaAccount": CreateSocialMediaAccount(),
        "updateSocialMediaAccount": UpdateSocialMediaAccount(),
        "socialMediaAccount": currentPage,
    }

    return render(request, "gc/social-media-account.html", context)