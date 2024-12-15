from django.urls import path

from .views import BibliotecatView

urlpatterns = [
    path(
        "",
        BibliotecatView.as_view(),
        name="bibliotecas",
    ),
    # path("normativas/", include(("apps.biblioteca.normativas.urls", "normativas"))),
    # path(
    #     "api/normativas/",
    #     include(("apps.biblioteca.normativas.urls_apis", "api_normativas")),
    # ),
]
