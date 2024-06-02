
from django.shortcuts import render, redirect
from .forms import UsuarioForm, UsuarioAForm, UsuariosPForm, DepartamentosForm, DepartamentosEForm, SedesForm, SedesEForm
from .models import Usuarios, Departamentos, Sedes
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import get_template
from index.decorators import no_autenticado, allowed_users
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa

# VISTAS DE ADMIN
@login_required(login_url='login')
def usuarios(request):
    if request.method == 'POST':
        form1 = UsuarioForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect("/admin/usuarios#success")
        else:
            context = {'form1': form1}
            return redirect("/admin/usuarios#failed")
    departamentosp = Departamentos.objects.all()
    sedesp = Sedes.objects.all()
    usersl = Usuarios.objects.all()
    paginator = Paginator(usersl, 14) # 14 objetos por página
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
    context = {'form1': UsuarioForm(), 'usersl': pagina_actual, 'departamentosp': departamentosp, 'sedesp': sedesp}
    return render(request, 'usuarios.html', context)

# VISTAS DE ACTUALIZACIÓN DE USUARIOS - ADMIN
def update_usuarios(request, id):
    queryset = Usuarios.objects.get(id=id)
    forml = UsuarioAForm(instance=queryset)
    if request.method == 'POST':
        forml = UsuarioAForm(request.POST, instance=queryset)
        if forml.is_valid():
            forml.save()
            return redirect('/admin/usuarios#updatesuccess')

# VISTAS DE ACTUALIZACIÓN DE PASSWORD DE USUARIOS - ADMIN
def updatep_usuarios(request, id):
    queryset = Usuarios.objects.get(id=id)
    forml = UsuariosPForm(instance=queryset)
    if request.method == 'POST':
        forml = UsuariosPForm(request.POST, instance=queryset)
        if forml.is_valid():
            forml.save()
            return redirect('/admin/usuarios#updatesuccess')

# VISTAS DE ELIMINACIÓN DE USUARIOS - ADMIN
def del_usuarios(request, id):
    if request.method == 'POST':
        users = Usuarios.objects.get(id=id)
        users.delete()
        return redirect('/admin/usuarios#deletesuccess')

# VISTAS DE REGLAMENTOS - CONSULTAR
@login_required(login_url='login')
def usuarios_consultar(request, accion):
    if accion == 'consultar':
        if 'username' in request.GET:
            username = request.GET['username']
            usersl = Usuarios.objects.filter(username=username)
    context = {'form1': UsuarioForm(), 'forml': UsuarioAForm(), 'usersl': usersl}
    return render(request, 'usuarios.html', context)

# VISTAS DE CREACIÓN Y LISTA DE DEPARTAMENTOS - ADMIN
@login_required(login_url='login')
def departamentos(request):
    if request.method == 'POST':
        form6 = DepartamentosForm(request.POST)
        if form6.is_valid():
            form6.save()
            return redirect("/admin/departamentos#addsuccess")
        else:
            context = {'form6': form6}
            return render(request, 'departamentos.html', context)
    departamentosp = Departamentos.objects.all()
    paginator = Paginator(departamentosp, 14) # 14 objetos por página
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
    context = {'formdp': DepartamentosEForm(),'form6': DepartamentosForm(), 'departamentosp': pagina_actual}
    return render(request, 'departamentos.html', context)

# VISTAS DE ACTUALIZACIÓN DE DEPARTAMENTOS - ADMIN
def update_departamentos(request, id):
    queryset = Departamentos.objects.get(id=id)
    form = DepartamentosEForm(instance=queryset)
    if request.method == 'POST':
        form = DepartamentosEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/admin/departamentos#updatesuccess')

# VISTAS DE ELIMINACIÓN DE DEPARTAMENTOS - ADMIN
def del_departamentos(request, id):
    if request.method == 'POST':
        form = Departamentos.objects.get(id=id)
        form.delete()
        return redirect('/admin/departamentos#deletesuccess')

# VISTAS DE DEPARTAMENTOS - CONSULTAR
@login_required(login_url='login')
def departamentos_consultar(request, accion):
    if accion == 'consultar':
        if 'estado' in request.GET:
            estado = request.GET['estado']
            departamentoss = Departamentos.objects.filter(estado=estado)
            paginator = Paginator(departamentoss, 15) # 14 objetos por página
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
    context = {'form6': DepartamentosForm(), 'formdp': DepartamentosEForm(), 'departamentoss': pagina_actual}
    return render(request, 'departamentos.html', context)

# VISTAS DE CREACIÓN Y LISTA DE SEDES - ADMIN
@login_required(login_url='login')
def sedes(request):
    if request.method == 'POST':
        form7 = SedesForm(request.POST)
        if form7.is_valid():
            form7.save()
            return redirect("/admin/sedes#success")
        else:
            context = {'form7': form7}
            return render(request, 'sedes.html', context)
    sedesp = Sedes.objects.all()
    context = {'form7': SedesForm(), 'formsp': SedesEForm(), 'sedesp': sedesp}
    return render(request, 'sedes.html', context)

# VISTAS DE ACTUALIZACIÓN DE SEDES - ADMIN
def update_sedes(request, id):
    queryset = Sedes.objects.get(id=id)
    form = SedesEForm(instance=queryset)
    if request.method == 'POST':
        form = SedesEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/admin/sedes#updatesuccess')

# VISTAS DE ELIMINACIÓN DE SEDES - ADMIN
def del_sedes(request, id):
    if request.method == 'POST':
        form = Sedes.objects.get(id=id)
        form.delete()
        return redirect('/admin/sedes#deletesuccess')

# VISTAS DE SEDES - CONSULTAR
@login_required(login_url='login')
def sedes_consultar(request, accion):
    if accion == 'consultar':
        if 'departamento' in request.GET:
            departamento = request.GET['departamento']
            sedess = Sedes.objects.filter(departamento=departamento)
            paginator = Paginator(sedess, 15) # 14 objetos por página
            pagina = request.GET.get('page')
            try:
                # Obtener la página solicitada
                pagina_actual = paginator.page(pagina)
            except PageNotAnInteger:
                # Si la página no es un entero, redirigir a la primera páginas
                pagina_actual = paginator.page(1)
            except EmptyPage:
                # Si la página está fuera de rango, redirigir a la última página
                pagina_actual = paginator.page(paginator.num_pages)
    context = {'form7': SedesForm(), 'formsp': SedesEForm(), 'sedess': pagina_actual}
    return render(request, 'sedes.html', context)