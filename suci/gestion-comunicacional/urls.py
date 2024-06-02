from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="gc-index"),
    path("social-media-account", views.listingSocialMediaAccount, name="gc-listing-social-media-account"),
    path("social-media-account/<str:accion>", views.listingSocialMediaAccount, name="gc-filter-social-media-account"),
    path("social-media-account/detalle/<int:id>", views.readerSocialMediaAccount, name="gc-reader-social-media-account"),
    path("social-media-account/actualizar/<int:id>", views.updaterSocialMediaAccount, name="gc-updater-social-media-account"),
    path("social-media-account/eliminar/<int:id>", views.destroyerSocialMediaAccount, name="gc-destroyer-social-media-account"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
