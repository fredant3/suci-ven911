from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from gestion_comunicacional.info.InfoController import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="info"),
    path("equipments/", include(("gestion_comunicacional.equipments.urls", "eq"))),
    path("social-media/", include(("gestion_comunicacional.social_media.urls", "sm"))),
    path(
        "social-activity/",
        include(("gestion_comunicacional.social_activity.urls", "sa")),
    ),
]
