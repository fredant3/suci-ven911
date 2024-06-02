from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("modulos", views.modulos, name="modulos"),
    path("login", views.loginf, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("403", views.loginf403, name="403"),
    path("correo", views.correo, name="correo"),
    path("recuperar-password", views.recuperar, name="recuperar-password"),
]
