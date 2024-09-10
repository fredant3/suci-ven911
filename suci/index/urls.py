from django.urls import include, path

urlpatterns = [
    path("auth/", include(("index.authentication.urls", "auth"))),
    path("modules/", include(("index.modules.urls", "modules"))),
]
