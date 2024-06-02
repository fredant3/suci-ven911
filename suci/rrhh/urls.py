from django.urls import path
from .import views

urlpatterns = [
    path('', views.personal, name="ingresosPersonal"),
    path('personalRetirado', views.personalRetirado, name="personalRetirado"),
    path('personalVacaciones', views.personalVacaciones, name="personalVacaciones"),
    path('descargar-excel/', views.descargar_excel, name='descargar-excel'),
    path('descargar-excel-retirados/', views.descargar_excel_retirados, name='descargar-excel-retirados'),
    path('descargar-excel-vacaciones/', views.descargar_excel_vacaciones, name='descargar-excel-vacaciones'),
    #URLS DE MANTENIMIENTO
    path('estadocivil/', views.estadoCivil, name="estadoCivil"),
    path('genero/', views.mantSexo, name="genero"),
    path('tallaCamisa/', views.mantTallaCamisa, name="tallaCamisa"),
    path('tallaPantalon/', views.mantTallaPantalon, name="tallaPantalon"),
    path('tallaZapato/', views.mantTallaZapato, name="tallaZapato"),
    path('gradoInstruccion/', views.mantGrado, name="gradoInstruccion"),
    path('tipoPersonal/', views.mantTipoPersonal, name="tipoPersonal"),
    path('cargo/', views.mantCargo, name="cargo"),
    path('departamento/', views.mantDepartamento, name="departamento"),
    path('sedes/', views.mantSedes, name="sede"),
]

