from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('usuarios/', views.usuarios, name="usuarios"),
    path('usuarios<str:accion>', views.usuarios_consultar, name="usuarios_consultar"),
    path('usuarios/update/<int:id>', views.update_usuarios, name="update_usuarios"),
    path('usuarios/updatep/<int:id>', views.updatep_usuarios, name="updatep_usuarios"),
    path('usuarios/delete/<int:id>', views.del_usuarios, name="del_usuarios"),
    path('departamentos', views.departamentos, name="departamentos"),
    path('departamentos/update/<int:id>', views.update_departamentos, name="update_departamentos"),
    path('departamentos/delete/<int:id>', views.del_departamentos, name="del_departamentos"),
    path('departamentos<str:accion>', views.departamentos_consultar, name="departamentos_consultar"),
    path('sedes', views.sedes, name="sedes"),
    path('sedes<str:accion>', views.sedes_consultar, name="sedes_consultar"),
    path('sedes/update/<int:id>', views.update_sedes, name="update_sedes"),
    path('sedes/delete/<int:id>', views.del_sedes, name="del_sedes"),
    path('sedes<str:accion>', views.sedes_consultar, name="sedes_consultar"),
]