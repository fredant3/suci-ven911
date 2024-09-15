from django.urls import path

urlpatterns = [
    path(
        "account",
        ListSocialMediaAccount.as_view(),
        name="listing-account",
    ),
    # path('denuncias/', views.denuncia, name="denuncia"),
    path("denuncias/<str:accion>/", views.denuncia, name="denuncias"),
    path(
        "obtener-datos-denuncia-edicion/<int:denuncia_id>/",
        views.obtener_datos_denuncia_edicion,
        name="obtener-datos-denuncia-edicion",
    ),
    path(
        "descargar-excel-denuncias/",
        views.descargar_excel_denuncias,
        name="descargar-excel-denuncias",
    ),
    path("registros/<str:accion>/", views.registroFilmico, name="registros"),
    path(
        "obtener-datos-registro-edicion/<int:registro_id>/",
        views.obtener_datos_registro_edicion,
        name="obtener-datos-registro-edicion",
    ),
    path(
        "descargar-excel-registro/",
        views.descargar_excel_registros,
        name="descargar-excel-R",
    ),
]
