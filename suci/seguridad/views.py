from django.shortcuts import render, redirect, HttpResponse
from .forms import EntradapForm, EntradapEForm, SalidapForm, SalidapEForm, GestionForm, GestionEForm, AmbulanciaForm, AmbulanciaEForm
from .models import  Entradap, Salidap, Gestion, Ambulancia, Patrulla, Particular
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from index.decorators import no_autenticado, allowed_users
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa

# VISTAS DE SEGURIDAD
@login_required(login_url='login')
def seguridad(request):
    entradap = Entradap.objects.all()
    salidap = Salidap.objects.all()
    gestion = Gestion.objects.all()
    objetos = zip(entradap, salidap)
    context = {'gestion': gestion, 'entradap': entradap, 'salidap': salidap,'objetos': objetos }
    return render(request, "seguridad.html", context)

# VISTAS DE ENTRADA DE PERSONAL
@login_required(login_url='login')
def entradap(request):
    if request.method == 'POST':
        form2 = EntradapForm(request.POST)
        if form2.is_valid():
            form2.save()
        else:
            context = {'form2': form2}
            return render(request, 'entradap.html', context)
    entradapp = Entradap.objects.all()
    paginator = Paginator(entradapp, 15) # 10 objetos por página
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
    context = {'form2': EntradapForm(), 'formeep': EntradapEForm(), 'entradapp': pagina_actual}
    return render(request, 'entradap.html', context)

# VISTAS DE ACTUALIZACIÓN DE ENTRADA DE PERSONAL
def update_entradap(request, id):
    queryset = Entradap.objects.get(id=id)
    form = EntradapEForm(instance=queryset)
    if request.method == 'POST':
        form = EntradapEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/entradap#updatesuccess')

# VISTAS DE ELIMINACIÓN DE ENTRADA DE PERSONAL
def del_entradap(request, id):
    if request.method == 'POST':
        form = Entradap.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/entradap#deletesuccess')
    
# VISTAS DE SALIDA DE PERSONAL
@login_required(login_url='login')
def salidap(request):
    if request.method == 'POST':
        form3 = SalidapForm(request.POST)
        if form3.is_valid():
            form3.save()
        else:
            context = {'form3': form3}
            return render(request, 'salidap.html', context)
    salidapp = Salidap.objects.all()
    paginator = Paginator(salidapp, 15) # 10 objetos por página
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
    context = {'form2': SalidapForm(), 'formesp': SalidapEForm(), 'salidapp': pagina_actual}
    return render(request, 'salidap.html', context)

# VISTAS DE SALIDA - CONSULTAR
@login_required(login_url='login')
def salidap_consultar(request, accion):
    if accion == 'consultar':
        if 'name' in request.GET:
            name = request.GET['name']
            pagina_actual = Entradap.objects.filter(name=name)
    context = {'form2': SalidapForm(), 'formesp': SalidapEForm(), 'salidapp': pagina_actual}
    return render(request, 'salidap.html', context)
    
# VISTAS DE ACTUALIZACIÓN DE SALIDA DE PERSONAL
def update_salidap(request, id):
    queryset = Salidap.objects.get(id=id)
    form = SalidapEForm(instance=queryset)
    if request.method == 'POST':
        form = SalidapEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/salidap#updatesuccess')

# VISTAS DE ELIMINACIÓN DE SALIDA DE PERSONAL
def del_salidap(request, id):
    if request.method == 'POST':
        form = Salidap.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/salidap#deletesuccess')
  
# VISTAS DE GESTIÓN DE INCIDENTES
@login_required(login_url='login')
def gestion(request):
    if request.method == 'POST':
        form2 = GestionForm(request.POST)
        if form2.is_valid():
            form2.save()
        else:
            context = {'form2': form2}
            return render(request, 'gestion.html', context)
    gestionp = Gestion.objects.all()
    paginator = Paginator(gestionp, 15) # 10 objetos por página
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
    context = {'form2': GestionForm(), 'formesp': GestionEForm(), 'gestionp': pagina_actual}
    return render(request, 'gestion.html', context)

# VISTAS DE GESTION - CONSULTAR
@login_required(login_url='login')
def gestion_consultar(request, accion):
    if accion == 'consultar':
        if 'name' in request.GET:
            name = request.GET['name']
            pagina_actual = Gestion.objects.filter(name=name)
    context = {'form2': GestionForm(), 'formesp': GestionEForm(), 'gestionp': pagina_actual}      
    return render(request, 'gestion.html', context)

# VISTAS DE ACTUALIZACIÓN DE GESTIÓN DE INCIDENTES
def update_gestion(request, id):
    queryset = Gestion.objects.get(id=id)
    form = GestionEForm(instance=queryset)
    if request.method == 'POST':
        form = GestionEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/gestion#updatesuccess')

# VISTAS DE ELIMINACIÓN DE GESTIÓN DE INCIDENTES
def del_gestion(request, id):
    if request.method == 'POST':
        form = Gestion.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/gestion#deletesuccess')

#VISTAS DE AMBULANCIA
@login_required(login_url='login')
def ambulancia(request):
    if request.method == 'POST':
        form11 = AmbulanciaForm(request.POST)
        if form11.is_valid():
            form11.save()
        else:
            context = {'form11': form11}
            return render(request, 'ambulancia.html', context)
    ambulanciaa = Ambulancia.objects.all()
    paginator = Paginator(ambulanciaa, 15) # 10 objetos por página
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
    context = {'form11':AmbulanciaForm (), 'forma':AmbulanciaEForm (), 'ambulanciaa': pagina_actual}
    return render(request, 'ambulancia.html', context)

# VISTAS DE ACTUALIZACIÓN DE ENTRADA DE PERSONAL
def update_ambulancia(request, id):
    queryset = Ambulancia.objects.get(id=id)
    form = AmbulanciaEForm(instance=queryset)
    if request.method == 'POST':
        form = AmbulanciaEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/ambulancia#updatesuccess')

# VISTAS DE ELIMINACIÓN DE ENTRADA DE PERSONAL
def del_ambulancia(request, id):
    if request.method == 'POST':
        form = Ambulancia.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/ambulancia#deletesuccess')
    
# VISTAS DE SEGURIDAD - CONSULTAR - AMBULANCIA
def ambulancia_consultar(request, accion):
    if accion == 'consultar':
        if 'cedula' in request.GET:
            cedula = request.GET['cedula']
            ambulanciaa = Ambulancia.objects.filter(cedula=cedula)
            paginator = Paginator(ambulanciaa, 5) # 14 objetos por página
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
        context = {'form11': AmbulanciaForm(), 'forma': AmbulanciaEForm (), 'ambulanciaa': pagina_actual}
        return render(request, 'ambulancia.html', context)




