"""
URL configuration for suci project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("apps.users.auth.urls", "auth"))),
    path("api/auth/", include(("apps.users.auth.urls_apis", "api_auth"))),
    path("dashboard/", include(("apps.dashboard.modules.urls", "modules"))),
    path("gestion-administrativa/", include(("apps.administracion.urls"))),
    path("asesoria-juridica/", include(("apps.asesoria.urls"))),
    path("biblioteca/", include(("apps.biblioteca.urls"))),
    path("organizacion/", include(("apps.organizacion.urls"))),
    path("emergencia/", include(("apps.emergencia.urls"))),
    path("planificacion/", include(("apps.planificacion.urls"))),
    path("potencia/", include(("apps.potencia.urls"))),
    path("gestion-humana/", include(("apps.rrhh.urls"))),
    path("", RedirectView.as_view(url="dashboard", permanent=True)),
]
