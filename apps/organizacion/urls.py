from django.urls import include, path

urlpatterns = [
    path(
        "reglamentos/", include(("apps.organizacion.reglamentos.urls", "reglamentos"))
    ),
    path(
        "api/reglamentos/",
        include(("apps.organizacion.reglamentos.urls_apis", "api_reglamentos")),
    ),
]
