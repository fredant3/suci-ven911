from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import CreateSocialMediaAccount, UpdateSocialMediaAccount
from .models import SocialMediaAccount


@login_required(login_url="login")
def index(request):
    return render(request, "gc/index.html")


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


@login_required(login_url="login")
def readerSocialMediaAccount(request):
    if request.method == "POST":
        createSocialMediaAccount = CreateSocialMediaAccount(request.POST)
        if createSocialMediaAccount.is_valid():
            createSocialMediaAccount.save()
        else:
            context = {"createSocialMediaAccount": createSocialMediaAccount}
            return render(request, "gc/social-media-account.html", context)

    socialMediaAccount = SocialMediaAccount.objects.all()
    paginator = Paginator(socialMediaAccount, 15)
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


@login_required(login_url="login")
def updaterSocialMediaAccount(request, id):
    if request.method == "PUT":
        return redirect("/gestion-comunicacional/social-media-account#updateerror")

    queryset = SocialMediaAccount.objects.get(id=id)
    form = UpdateSocialMediaAccount(instance=queryset)

    form = UpdateSocialMediaAccount(request.PUT, instance=queryset)
    if form.is_valid():
        form.save()
        return redirect("/gestion-comunicacional/social-media-account#updatesuccess")


@login_required(login_url="login")
def destroyerSocialMediaAccount(request, id):
    if request.method == "DELETE":
        return redirect("/gestion-comunicacional/social-media-account#deleteerror")

    form = SocialMediaAccount.objects.get(id=id)
    form.delete()
    return redirect("/gestion-comunicacional/social-media-account#deletesuccess")
