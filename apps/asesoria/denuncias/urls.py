from django.urls import path

from .views.create_view import DenunciaCreateView
from .views.list_view import DenunciaListView
from .views.update_view import DenunciaUpdateView

urlpatterns = [
    path(
        "",
        DenunciaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        DenunciaCreateView.as_view(),
        name="create",
    ),
    path(
        "read",
        DenunciaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        DenunciaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DenunciaListView.as_view(),
        name="delete",
    ),
    # path('denuncias/', views.denuncia, name="denuncia"),
    # path("denuncias/<str:accion>/", views.denuncia, name="denuncias"),
    # path(
    #     "obtener-datos-denuncia-edicion/<int:denuncia_id>/",
    #     views.obtener_datos_denuncia_edicion,
    #     name="obtener-datos-denuncia-edicion",
    # ),
    # path(
    #     "descargar-excel-denuncias/",
    #     views.descargar_excel_denuncias,
    #     name="descargar-excel-denuncias",
    # ),
]
