from django.urls import path
from  .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('seguridad/', views.seguridad, name="seguridad"),
    path('entradap/', views.entradap, name="entradap"),
    #path('entradap<str:accion>', views.entradap_consultar, name="entradap_consultar"),
    path('entradap/update/<int:id>', views.update_entradap, name="update_entradap"),
    path('entradap/delete/<int:id>', views.del_entradap, name="del_entradap"),
    path('salidap', views.salidap, name="salidap"),
    path('salidap<str:accion>', views.salidap_consultar, name="salidap_consultar"),
    path('salidap/update/<int:id>', views.update_salidap, name="update_salidap"),
    path('salidap/delete/<int:id>', views.del_salidap, name="del_salidap"),
    path('gestion/', views.gestion, name="gestion"),
    path('gestion/<str:accion>', views.gestion_consultar, name="gestion_consultar"),
    path('gestion/update/<int:id>', views.update_gestion, name="update_gestion"),
    path('gestion/delete/<int:id>', views.del_gestion, name="del_gestion"),
    path('ambulancia/', views.ambulancia, name="ambulancia"),
    path('ambulancia<str:accion>', views.ambulancia_consultar, name="ambulancia_consultar"),
    path('ambulancia/update/<int:id>', views.update_ambulancia, name="update_ambulancia"),
    path('ambulancia/delete/<int:id>', views.del_ambulancia, name="del_ambulancia"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

