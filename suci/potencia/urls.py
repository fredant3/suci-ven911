from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home, name="Inicio"),
    path('incidencia',views.Incidencia, name="Incidencia"),
    path('estatus',views.Estatus, name="Estatus"),
    path('reportes',views.Reportes, name="Reportes"),
    path('registrarIncidencias/', views.FormularioIncidencias, name= 'registrarIncidencias'),
]