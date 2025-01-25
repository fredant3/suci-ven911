from django.urls import path
from organizacion.normativas.views.create_view import NormativaCreateApiView
from organizacion.normativas.views.delete_view import NormativaDeleteApiView
from organizacion.normativas.views.list_view import NormativaListApiView
from organizacion.normativas.views.update_view import NormativaUpdateApiView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(
        "",
        NormativaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        NormativaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        NormativaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        NormativaDeleteApiView.as_view(),
        name="delete",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)