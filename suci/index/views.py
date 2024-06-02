from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .decorators import no_autenticado, allowed_users
from django.contrib.auth.decorators import login_required

# VISTAS DE INDEX
@login_required(login_url='login')
def index(request):
    return render(request, "modulos.html")

@login_required(login_url='login')
def modulos(request):
    return render(request, "modulos.html")

# VISTA DE RECUPERAR CONTRASEÑA
def recuperar(request):
    return render(request, "public/recuperar-password.html")

# VISTA DE ENVIO DE CORREO
def correo(request):
    return render(request, "public/correo.html")

# VISTAS DE 403
def loginf403(request):
    return render(request, "403.html")

# VISTAS DE INDEX
@no_autenticado
def loginf(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/modulos')
        else:
            return render(request, "public/login_error.html")
    
    context = {}
    return render(request, "public/login.html", context)

# VISTAS DE LOGOUT 
def logoutUser(request):
    logout(request)
    return redirect('/')