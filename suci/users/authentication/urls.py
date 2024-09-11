from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.authentication.controllers.controller import AuthView
from users.authentication.controllers.LoginController import LoginController

urlpatterns = [
    # FRONTEND
    path(
        "login",
        LoginController.as_view(template_name="public/authentication/login.html"),
        name="login",
    ),
    path(
        "logout",
        LogoutView.as_view(next_page=reverse_lazy(settings.LOGIN_URL)),
        name="logout",
    ),
    path(
        "forgot-password",
        AuthView.as_view(template_name="public/authentication/forgot_password.html"),
        name="forgot-password",
    ),
    path(
        "register",
        AuthView.as_view(template_name="public/authentication/register.html"),
        name="register",
    ),
    # API
    path("api/login", TokenObtainPairView.as_view(), name="api_login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
