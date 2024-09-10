from django.urls import include, path

urlpatterns = [
    path("modules/", include(("index.modules.urls", "modules"))),
]
