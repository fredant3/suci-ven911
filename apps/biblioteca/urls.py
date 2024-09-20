from django.urls import include, path

urlpatterns = [
    path("normativas/", include(("apps.biblioteca.normativas.urls", "normativas"))),
    path(
        "api/normativas/",
        include(("apps.biblioteca.normativas.urls_apis", "api_normativas")),
    ),
]
