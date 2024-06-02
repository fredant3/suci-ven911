from django.shortcuts import render, redirect
from .forms import (
    ReglamentsForm,
    ReglamentsUForm,
    ReglamentsUFForm,
    NormativasUForm,
    NormativasUFForm,
    NormativasForm,
)
from .models import Reglamentos, Normativas
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


# VISTAS DE ORGANIZACIÓN
@login_required(login_url="login")
def organizacion(request):
    reglamentoss = Reglamentos.objects.all()
    normativass = Normativas.objects.all()
    objetos = zip(reglamentoss, normativass)
    context = {
        "reglamentoss": reglamentoss,
        "normativass": normativass,
        "objetos": objetos,
    }
    return render(request, "organizacion/organizacion.html", context)


# VISTAS DE ORGANIZACIÓN
@login_required(login_url="login")
def organizacion(request):
    reglamentoss = Reglamentos.objects.all()
    normativass = Normativas.objects.all()
    objetos = zip(reglamentoss, normativass)
    context = {
        "reglamentoss": reglamentoss,
        "normativass": normativass,
        "objetos": objetos,
    }
    return render(request, "organizacion/organizacion.html", context)


# VISTAS DE NORMATIVAS
@login_required(login_url="login")
def normativas(request):
    if request.method == "POST":
        form5 = NormativasForm(request.POST, request.FILES)
        if form5.is_valid():
            form5.save()
            return redirect("/organizacion/normativas#success")
        else:
            context = {"form5": form5}
            return render(request, "organizacion/organizacion/normativas.html", context)
    normativass = Normativas.objects.all()
    paginator = Paginator(normativass, 14)  # 14 objetos por página
    pagina = request.GET.get("page")
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = paginator.page(paginator.num_pages)
    context = {
        "form5": NormativasForm(),
        "formen": NormativasUForm(),
        "formenf": NormativasUFForm(),
        "normativass": pagina_actual,
    }
    return render(request, "organizacion/normativas.html", context)


# VISTAS DE NORMATIVAS - CONSULTAR
@login_required(login_url="login")
def normativas_consultar(request, accion):
    if accion == "consultar":
        if "name" in request.GET:
            name = request.GET["name"]
            normativass = Normativas.objects.filter(name=name)
            paginator = Paginator(normativass, 5)  # 14 objetos por página
            pagina = request.GET.get("page")
            try:
                # Obtener la página solicitada
                pagina_actual = paginator.page(pagina)
            except PageNotAnInteger:
                # Si la página no es un entero, redirigir a la primera página
                pagina_actual = paginator.page(1)
            except EmptyPage:
                # Si la página está fuera de rango, redirigir a la última página
                pagina_actual = paginator.page(paginator.num_pages)
    context = {
        "form5": NormativasForm(),
        "formen": NormativasUForm(),
        "formenf": NormativasUFForm(),
        "normativass": pagina_actual,
    }
    return render(request, "organizacion/normativas.html", context)


# VISTAS DE ACTUALIZACIÓN DE NORMATIVAS
@login_required(login_url="login")
def update_normativas(request, id):
    queryset = Normativas.objects.get(id=id)
    form = NormativasUForm(instance=queryset)
    if request.method == "POST":
        form = ReglamentsUForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("/organizacion/normativas#updatesuccess")


# VISTAS DE ACTUALIZACIÓN DE ARCHIVOS DE NORMATIVAS
@login_required(login_url="login")
def updatef_normativas(request, id):
    queryset = Normativas.objects.get(id=id)
    form = NormativasUFForm(instance=queryset)
    if request.method == "POST":
        form = NormativasUFForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("/organizacion/normativas#updatesuccess")


# VISTAS DE ELIMINACIÓN DE NORMATIVAS
@login_required(login_url="login")
def del_normativas(request, id):
    if request.method == "POST":
        form = Normativas.objects.get(id=id)
        form.delete()
        return redirect("/organizacion/normativas#deletesuccess")


# VISTAS DE REGLAMENTOS
@login_required(login_url="login")
def reglamentos(request):
    if request.method == "POST":
        form = ReglamentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {"form": form}
            return render(request, "organizacion/reglamentos.html", context)
    reglamentoss = Reglamentos.objects.all()
    paginator = Paginator(reglamentoss, 14)  # 10 objetos por página
    pagina = request.GET.get("page")
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = paginator.page(paginator.num_pages)
    context = {
        "form": ReglamentsForm(),
        "former": ReglamentsUForm(),
        "formerf": ReglamentsUFForm(),
        "reglamentoss": pagina_actual,
    }
    return render(request, "organizacion/reglamentos.html", context)


# VISTAS DE REGLAMENTOS - CONSULTAR
@login_required(login_url="login")
def reglamentos_consultar(request, accion):
    if accion == "consultar":
        if "name" in request.GET:
            name = request.GET["name"]
            reglamentoss = Reglamentos.objects.filter(name=name)
    context = {
        "form": ReglamentsForm(),
        "former": ReglamentsUForm(),
        "formerf": ReglamentsUFForm(),
        "reglamentoss": reglamentoss,
    }
    return render(request, "organizacion/reglamentos.html", context)


# VISTAS DE ACTUALIZACIÓN DE REGLAMENTOS
@login_required(login_url="login")
def update_reglamentos(request, id):
    queryset = Reglamentos.objects.get(id=id)
    form = ReglamentsUForm(instance=queryset)
    if request.method == "POST":
        form = ReglamentsUForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("/organizacion/reglamentos#updatesuccess")


# VISTAS DE ACTUALIZACIÓN DE ARCHIVOS DE REGLAMENTOS
@login_required(login_url="login")
def update_reglamentosf(request, id):
    queryset = Reglamentos.objects.get(id=id)
    form = ReglamentsUFForm(instance=queryset)
    if request.method == "POST":
        form = ReglamentsUFForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("/organizacion/reglamentos#updatesuccess")


# VISTAS DE ELIMINACIÓN DE REGLAMENTOS
@login_required(login_url="login")
def del_reglamentos(request, id):
    if request.method == "POST":
        form = Reglamentos.objects.get(id=id)
        form.delete()
        return redirect("/organizacion/reglamentos#deletesuccess")


# VISTAS DE BIBLIOTECA - REGLAMENTOS - PUBLICAR
@login_required(login_url="login")
def pubublicar_reglamento(request, id):
    queryset = Reglamentos.objects.get(id=id)
    if request.method == "POST":
        queryset.estado = True
        queryset.save()
        return redirect("/organizacion/reglamentos#updatesuccess")


# VISTAS DE BIBLIOTECA - REGLAMENTOS - DESPUBLICAR
@login_required(login_url="login")
def despubublicar_reglamento(request, id):
    queryset = Reglamentos.objects.get(id=id)
    if request.method == "POST":
        queryset.estado = False
        queryset.save()
        return redirect("/organizacion/reglamentos#updatesuccess")


# VISTAS DE BIBLIOTECA - NORMATIVAS - PUBLICAR
@login_required(login_url="login")
def pubublicar_normativas(request, id):
    queryset = Normativas.objects.get(id=id)
    if request.method == "POST":
        queryset.estado = True
        queryset.save()
        return redirect("/organizacion/normativas#updatesuccess")


# VISTAS DE BIBLIOTECA - NORMATIVAS - DESPUBLICAR
@login_required(login_url="login")
def despubublicar_normativas(request, id):
    queryset = Normativas.objects.get(id=id)
    if request.method == "POST":
        queryset.estado = False
        queryset.save()
        return redirect("/organizacion/normativas#updatesuccess")
