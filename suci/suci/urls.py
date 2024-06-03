"""
URL configuration for suci project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('4dm1n/', admin.site.urls),
    path("", include("organizacion.urls")),
    path("", include("presupuesto.urls")),
    path("presupuesto/", include("presupuesto.urls")),
    path("", include("paneluser.urls")),
    path("admin/", include("paneluser.urls")),
    path("", include("seguridad.urls")),
    path("seguridad/", include("seguridad.urls")),
    path("", include("planificacion.urls")),
    path("planificacion/", include("planificacion.urls")),
    path("", include("rrhh.urls")),
    path("rrhh/", include("rrhh.urls")),
    path("", include("potencia.urls")),
    path("potencia/", include("potencia.urls")),
    path("", include("index.urls")),
    path("biblioteca/", include("biblioteca.urls")),
    path("emergencia/", include("emergencia.urls")),
    path("organizacion/", include("organizacion.urls")),
    path("gestion-comunicacional/", include("gestion_comunicacional.urls")),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
