# Equipment
# Equipment Loan
from gestion_comunicacional.equipments.controllers.EquipmentLoanController import (
    CreateEquipmentLoan,
    DeleteEquipmentLoan,
    ListEquipmentLoan,
    ReadEquipmentLoan,
    UpdateEquipmentLoan,
)
from gestion_comunicacional.equipments.controllers.equipments.CreateEquipmentController import CreateEquipment
from gestion_comunicacional.equipments.controllers.equipments.DeleteEquipmentController import DeleteEquipment
from gestion_comunicacional.equipments.controllers.equipments.ListEquipmentController import ListEquipment
from gestion_comunicacional.equipments.controllers.equipments.UpdateEquipmentController import UpdateEquipment

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    # BEGING Equipment
    path(
        "",
        ListEquipment.as_view(),
        name="listing-equipments",
    ),
    path(
        "crear",
        CreateEquipment.as_view(),
        name="create-equipments",
    ),
    # path(
    #     "<int:pk>",
    #     ReadEquipment.as_view(),
    #     name="reader-equipments",
    # ),
    path(
        "<int:pk>/actualizar",
        UpdateEquipment.as_view(),
        name="updater-equipments",
    ),
    path(
        "<int:pk>/eliminar",
        DeleteEquipment.as_view(),
        name="destroyer-equipments",
    ),
    # BEGING Equipment Loan
    path(
        "loan",
        ListEquipmentLoan.as_view(),
        name="listing-loan",
    ),
    path(
        "loan/<str:accion>",
        ListEquipmentLoan.as_view(),
        name="filter-loan",
    ),
    path(
        "loan/crear",
        CreateEquipmentLoan.as_view(),
        name="create-loan",
    ),
    path(
        "loan/detalle/<int:pk>",
        ReadEquipmentLoan.as_view(),
        name="reader-loan",
    ),
    path(
        "loan/actualizar/<int:pk>",
        UpdateEquipmentLoan.as_view(),
        name="updater-loan",
    ),
    path(
        "loan/eliminar/<int:pk>",
        DeleteEquipmentLoan.as_view(),
        name="destroyer-loan",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
