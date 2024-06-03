from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .social_media.controllers.SocialMediaAccountController import (
    SocialMediaAccountController,
)

socialMediaAccountController = SocialMediaAccountController()

urlpatterns = [
    path("", views.index, name="gc-index"),
    path(
        "social-media-account",
        socialMediaAccountController.listing,
        name="gc-listing-social-media-account",
    ),
    path(
        "social-media-account/<str:accion>",
        socialMediaAccountController.listing,
        name="gc-filter-social-media-account",
    ),
    path(
        "social-media-account/crear",
        socialMediaAccountController.create,
        name="gc-create-social-media-account",
    ),
    path(
        "social-media-account/detalle/<int:id>",
        socialMediaAccountController.read,
        name="gc-reader-social-media-account",
    ),
    path(
        "social-media-account/actualizar/<int:id>",
        socialMediaAccountController.update,
        name="gc-updater-social-media-account",
    ),
    path(
        "social-media-account/eliminar/<int:id>",
        socialMediaAccountController.delete,
        name="gc-destroyer-social-media-account",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
