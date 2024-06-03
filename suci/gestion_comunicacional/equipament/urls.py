from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .controllers.EquipamentController import (
    CreateEquipament,
    DeleteEquipament,
    ListEquipament,
    ReadEquipament,
    UpdateEquipament,
)
from .controllers.EquipamentLoanController import (
    CreateEquipamentLoan,
    DeleteEquipamentLoan,
    ListEquipamentLoan,
    ReadEquipamentLoan,
    UpdateEquipamentLoan,
)

urlpatterns = [
    path(
        "",
        ListEquipament.as_view(),
        name="gc-listing-equipament",
    ),
    path(
        "<str:accion>",
        ListEquipament.as_view(),
        name="gc-filter-equipament",
    ),
    path(
        "crear",
        CreateEquipament.as_view(),
        name="gc-create-equipament",
    ),
    path(
        "detalle/<int:pk>",
        ReadEquipament.as_view(),
        name="gc-reader-equipament",
    ),
    path(
        "actualizar/<int:pk>",
        UpdateEquipament.as_view(),
        name="gc-updater-equipament",
    ),
    path(
        "eliminar/<int:pk>",
        DeleteEquipament.as_view(),
        name="gc-destroyer-equipament",
    ),
    path(
        "loan",
        ListEquipamentLoan.as_view(),
        name="gc-listing-loan-equipament",
    ),
    path(
        "loan/<str:accion>",
        ListEquipamentLoan.as_view(),
        name="gc-filter-equipament-loan",
    ),
    path(
        "loan/crear",
        CreateEquipamentLoan.as_view(),
        name="gc-create-equipament-loan",
    ),
    path(
        "loan/detalle/<int:pk>",
        ReadEquipamentLoan.as_view(),
        name="gc-reader-equipament-loan",
    ),
    path(
        "loan/actualizar/<int:pk>",
        UpdateEquipamentLoan.as_view(),
        name="gc-updater-equipament-loan",
    ),
    path(
        "loan/eliminar/<int:pk>",
        DeleteEquipamentLoan.as_view(),
        name="gc-destroyer-equipament-loan",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
