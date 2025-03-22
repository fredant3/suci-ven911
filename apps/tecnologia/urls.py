from django.urls import include, path
from tecnologia.view import tecnologiaView

urlpatterns = [
    path(
        "tecnologia",
        tecnologiaView.as_view(),
        name="tecnologia",
    ),
    path("", include(("apps.tecnologia.urls_webs", "tecnologia"))),
    path(
        "api/tecnologia-de-informacion/",
        include(("apps.tecnologia.urls_apis", "api_tecnologia")),
    ),
    path("grupos/", include(("apps.tecnologia.groups.urls", "grupos"))),
    path(
        "api/grupos/",
        include(("apps.tecnologia.groups.urls_apis", "api_grupos")),
    ),
    path("usuarios/", include(("apps.tecnologia.usuarios.urls", "usuarios"))),
    path(
        "api/usuarios/",
        include(("apps.tecnologia.usuarios.urls_apis", "api_usuarios")),
    ),
]
