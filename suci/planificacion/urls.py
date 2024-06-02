from django.urls import path
from  .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('inicio/', views.planificacion_inicio, name="planificacion_inicio"),
    path('objetivos', views.objetivos, name="objetivos"),
    path('objetivos<str:accion>', views.objetivos_consultar, name="objetivos_consultar"),
    path('objetivos/update/<int:id>', views.update_objetivos, name="update_objetivos"),
    path('objetivos/delete/<int:id>', views.del_objetivos, name="del_objetivos"),
    path('actividades', views.actividades, name="actividades"),
    path('actividades<str:accion>', views.actividades_consultar, name="actividades_consultar"),
    path('actividades/update/<int:id>', views.update_actividades, name="update_actividades"),
    path('actividades/delete/<int:id>', views.del_actividades, name="del_actividades"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)