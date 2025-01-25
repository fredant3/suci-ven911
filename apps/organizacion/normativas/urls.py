from django.urls import path
from organizacion.normativas.views.create_view import NormativaCreateView
from organizacion.normativas.views.delete_view import NormativaDeleteView
from organizacion.normativas.views.list_view import NormativaListView
from organizacion.normativas.views.update_view import NormativaUpdateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(
        "",
        NormativaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        NormativaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        NormativaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        NormativaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        NormativaDeleteView.as_view(),
        name="delete",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)