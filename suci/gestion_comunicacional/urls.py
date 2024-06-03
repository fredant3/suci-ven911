from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .info.InfoController import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="gc-index"),
    path("social-media/", include("gestion_comunicacional.social_media.urls")),
    path("social-activity/", include("gestion_comunicacional.social_activity.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
