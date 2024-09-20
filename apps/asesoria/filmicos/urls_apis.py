from django.urls import path

from .views.create_view import RegistroFilmicoCreateApiView
from .views.delete_view import RegistroFilmicoDeleteApiView
from .views.export_view import RegistroFilmicoExcelView
from .views.list_view import RegistroFilmicoListApiView
from .views.update_view import RegistroFilmicoUpdateApiView

urlpatterns = [
    path(
        "",
        RegistroFilmicoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        RegistroFilmicoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        RegistroFilmicoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        RegistroFilmicoDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        RegistroFilmicoExcelView.as_view(),
        name="export_excel",
    ),
]
