from django.urls import path
from . import views

urlpatterns = [
    path("", views.organizacion, name="organizacion"),
    path("reglamentos", views.reglamentos, name="organizacion_reglamentos"),
    path("reglamentos<str:accion>", views.reglamentos_consultar, name="reglamentos_consultar"),
    path("reglamentos/update/<int:id>", views.update_reglamentos, name="update_reglamentos"),
    path("reglamentos/updatef/<int:id>", views.update_reglamentosf, name="update_reglamentosf"),
    path("reglamentos/delete/<int:id>", views.del_reglamentos, name="del_reglamentos"),
    path("reglamentos/pubublicar_reg/<int:id>", views.pubublicar_reglamento, name="pubublicar_reglamento"),
    path("reglamentos/despubublicar_reg/<int:id>", views.despubublicar_reglamento, name="despubublicar_reglamento"),
    path("normativas", views.normativas, name="organizacion_normativas"),
    path("normativas/<str:accion>", views.normativas_consultar, name="normativas_consultar"),
    path("normativas/update/<int:id>", views.update_normativas, name="update_normativas"),
    path("normativas/updatef/<int:id>", views.updatef_normativas, name="updatef_normativas"),
    path("normativas/delete/<int:id>", views.del_normativas, name="del_normativas"),
    path("normativas/pubublicar_reg/<int:id>", views.pubublicar_normativas, name="pubublicar_normativas"),
    path("normativas/despubublicar_reg/<int:id>", views.despubublicar_normativas, name="despubublicar_normativas"),
]
