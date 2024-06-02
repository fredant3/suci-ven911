from django.shortcuts import render
from organizacion.models import Normativas, Reglamentos
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


# VISTAS DE BIBLIOTECA
def biblioteca(request):
    return render(request, "biblioteca/biblioteca.html")


# VISTAS DE BIBLIOTECA - NORMATIVAS
def biblioteca_normativas(request):
    normativass = Normativas.objects.all().filter(estado=True)
    paginator = Paginator(normativass, 10)  # 10 objetos por página
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
    context = {"normativass": normativass}
    return render(request, "biblioteca/biblioteca_normativas.html", context)


# VISTAS DE BIBLIOTECA - NORMATIVAS - CONSULTAR
@login_required(login_url="login")
def biblioteca_normativas_consultar(request, accion):
    if accion == "consultar":
        if "name" in request.GET:
            name = request.GET["name"]
            normativasb = Normativas.objects.filter(name=name, estado=True)
            paginator = Paginator(normativasb, 12)  # 15 objetos por página
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
        context = {"normativass": pagina_actual}
        return render(request, "biblioteca/biblioteca_normativas.html", context)


# VISTAS DE BIBLIOTECA - REGLAMENTOS
def biblioteca_reglamentos(request):
    reglamentoss = Reglamentos.objects.all().filter(estado=True)
    paginator = Paginator(reglamentoss, 10)  # 10 objetos por página
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
    context = {"reglamentoss": pagina_actual}
    return render(request, "biblioteca/biblioteca_reglamentos.html", context)


# VISTAS DE BIBLIOTECA - NORMATIVAS - CONSULTAR
@login_required(login_url="login")
def biblioteca_reglamentos_consultar(request, accion):
    if accion == "consultar":
        if "name" in request.GET:
            name = request.GET["name"]
            reglamentosb = Reglamentos.objects.filter(name=name, estado=True)
            paginator = Paginator(reglamentosb, 12)  # 15 objetos por página
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
        context = {"reglamentos": pagina_actual}
        return render(request, "biblioteca/biblioteca_reglamentos.html", context)
