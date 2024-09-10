from django.urls import path
from index.modules.ModuleCardController import ModuleCard

urlpatterns = [
    path(
        "",
        ModuleCard.as_view(),
        name="module",
    ),
]
