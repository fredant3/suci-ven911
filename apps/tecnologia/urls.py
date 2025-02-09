from django.urls import include, path

urlpatterns = [
    path("", include(("apps.tecnologia.urls_webs", "tecnologia"))),
    path(
        "api/tecnologia-de-informacion/",
        include(("apps.tecnologia.urls_apis", "api_tecnologia")),
    ),
]
