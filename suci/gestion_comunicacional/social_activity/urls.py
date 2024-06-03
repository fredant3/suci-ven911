from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .controllers.SocialActivityController import (
    CreateSocialActivity,
    DeleteSocialActivity,
    ListSocialActivity,
    ReadSocialActivity,
    UpdateSocialActivity,
)

urlpatterns = [
    path(
        "",
        ListSocialActivity.as_view(),
        name="gc-listing-social-activity",
    ),
    path(
        "<str:accion>",
        ListSocialActivity.as_view(),
        name="gc-filter-social-activity",
    ),
    path(
        "crear",
        CreateSocialActivity.as_view(),
        name="gc-create-social-activity",
    ),
    path(
        "detalle/<int:pk>",
        ReadSocialActivity.as_view(),
        name="gc-reader-social-activity",
    ),
    path(
        "actualizar/<int:pk>",
        UpdateSocialActivity.as_view(),
        name="gc-updater-social-activity",
    ),
    path(
        "eliminar/<int:pk>",
        DeleteSocialActivity.as_view(),
        name="gc-destroyer-social-activity",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
