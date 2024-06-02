from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('iniciopre/', views.iniciopre, name="iniciopre"),
    path('acciones/', views.acciones, name="acciones"),
    path('acciones<str:accion>', views.acciones_consultar, name="acciones_consultar"),
    path('acciones/update/<int:id>', views.update_acciones, name="acciones_proyecto"),
    path('acciones/delete/<int:id>', views.del_acciones, name="del_acciones"),
    path('acciones/pdf/', views.acciones_pdf, name="acciones_pdf"),
    path('proyecto/', views.proyecto, name="proyecto"),
    path('proyecto<str:accion>', views.proyecto_consultar, name="proyecto_consultar"),
    path('proyecto/update/<int:id>', views.update_proyecto, name="update_proyecto"),
    path('proyecto/delete/<int:id>', views.del_proyecto, name="del_proyecto"),
    path('asignacion/<str:accion>', views.asignacion_consultar, name="asignacion_consultar"),
    path('asignacion', views.asignacion, name="asignacion"),
    path('asignacion/update/<int:id>', views.update_asignacion, name="update_asignacion"),
    path('asignacion/delete/<int:id>', views.del_asignacion, name="del_asignacion"),
    path('asignacion/pdf/', views.asignacion_pdf, name="asignacion_pdf"),
    path('cedente', views.cedente, name="cedente"),
    path('cedente/update/<int:id>', views.update_cedente, name="update_cedente"),
    path('cedente/delete/<int:id>', views.del_cedente, name="del_cedente"),
    path('cedente/<str:accion>', views.cedente_consultar, name="cedente_consultar"),
    path('cedente/pdf/', views.cedente_pdf, name="cedente_pdf"),
    path('receptor', views.receptor, name="receptor"),
    path('receptor/<str:accion>', views.receptor_consultar, name="receptor_consultar"),
    path('receptor/update/<int:id>', views.update_receptor, name="update_receptor"),
    path('receptor/delete/<int:id>', views.del_receptor, name="del_receptor"),
    path('receptor/pdf/', views.receptor_pdf, name="receptor_pdf"),
    path('proyecto/pdf/', views.generar_pdf, name="generar_pdf"),
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)