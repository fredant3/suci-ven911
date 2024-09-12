from django.urls import include, path

urlpatterns = [
    path("", include(("index.modules.urls", "modules"))),
]
