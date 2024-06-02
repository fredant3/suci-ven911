from django.urls import path
from  .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.biblioteca, name="biblioteca"),
    path('normativas', views.biblioteca_normativas, name="biblioteca_normativas"),
    path('normativas/<str:accion>', views.biblioteca_normativas_consultar, name="biblioteca_normativas_consultar"),
    path('reglamentos', views.biblioteca_reglamentos, name="biblioteca_reglamentos"),
    path('reglamentos/<str:accion>', views.biblioteca_reglamentos_consultar, name="biblioteca_reglamentos_consultar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
