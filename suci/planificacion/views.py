
from django.shortcuts import render, redirect
from .forms import ObjetivosForm, ObjetivosUForm, ActividadesForm, ActividadesUForm
from .models import Objetivos, Actividades
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import get_template
from index.decorators import no_autenticado, allowed_users
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa

# VISTAS DE PLANIFICACION
@login_required(login_url='login')
def planificacion_inicio(request):
        return render(request, 'iniciopla.html')

# VISTAS DE PLANIFICACION -  OBJETIVOS
@login_required(login_url='login')
def objetivos(request):
    if request.method == 'POST':
        form17 = ObjetivosForm(request.POST)
        if form17.is_valid():
            form17.save()
        else:
            context = {'form17': form17}
            return render(request, 'objetivos.html', context)
    objetivoss = Objetivos.objects.all()
    paginator = Paginator(objetivoss, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form17': ObjetivosForm(), 'formob': ObjetivosUForm(), 'objetivoss': pagina_actual}
    return render(request, 'objetivos.html', context)

# VISTAS DE PRESUPUESTO - CONSULTAR - PROYECTO
@login_required(login_url='login')
def objetivos_consultar(request, accion):
    if accion == 'consultar':
        if 'nombrep' in request.GET:
            nombrep = request.GET['nombrep']
            proyectoo = Objetivos.objects.filter(nombrep=nombrep)
            paginator = Paginator(proyectoo, 5) # 14 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form17': ObjetivosForm(), 'formob': ObjetivosUForm(), 'objetivoss': pagina_actual}
        return render(request, 'objetivos.html', context)

# VISTAS DE ACTUALIZACIÓN DE PRESUPUESTO - PROYECTO
def update_objetivos(request, id):
    queryset = Objetivos.objects.get(id=id)
    form17 = ObjetivosUForm(instance=queryset)
    if request.method == 'POST':
        form17 = ObjetivosUForm(request.POST, instance=queryset)
        if form17.is_valid():
            form17.save()
            return redirect('/planificacion/objetivos#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PRESUPUESTO - PROYECTO
def del_objetivos(request, id):
    if request.method == 'POST':
        form17 = Objetivos.objects.get(id=id)
        form17.delete()
        return redirect('/planificacion/objetivos#deletesuccess')
    
# VISTAS DE PLANIFICACION -  ACTIVIDADES
@login_required(login_url='login')
def actividades(request):
    if request.method == 'POST':
        form18 = ActividadesForm(request.POST)
        if form18.is_valid():
            form18.save()
            return redirect('/planificacion/actividades#updatesuccess')
        else:
            context = {'form18': form18}
            return render(request, 'planificacion/actividades.html', context)
    actividadess = Actividades.objects.all()
    paginator = Paginator(actividadess, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form18': ActividadesForm(), 'formac': ActividadesUForm(), 'actividadess': pagina_actual}
    return render(request, 'actividades.html', context)

# VISTAS DE PLANIFICACION - CONSULTAR - PROYECTO
@login_required(login_url='login')
def actividades_consultar(request, accion):
    if accion == 'consultar':
        if 'nombrep' in request.GET:
            nombrep = request.GET['nombrep']
            actividadess = Actividades.objects.filter(nombrep=nombrep)
            paginator = Paginator(actividadess, 15) # 14 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form18': ActividadesForm(), 'formac': ActividadesUForm(), 'actividadess': pagina_actual}
        return render(request, 'actividades.html', context)
    
# VISTAS DE ACTUALIZACIÓN DE PLANIFICACION - ACTIVIDADES
def update_actividades(request, id):
    queryset = Actividades.objects.get(id=id)
    form18 = ActividadesUForm(instance=queryset)
    if request.method == 'POST':
        form18 = ActividadesUForm(request.POST, instance=queryset)
        if form18.is_valid():
            form18.save()
            return redirect('/planificacion/actividades#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PLANIFICACION - ACTIVIDADES
def del_actividades(request, id):
    if request.method == 'POST':
        form18 = Actividades.objects.get(id=id)
        form18.delete()
        return redirect('/planificacion/actividades#deletesuccess')