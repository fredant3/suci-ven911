from django.urls import path
from tecnologia.usuarios.views.create_view import UserCreateApiView
from tecnologia.usuarios.views.delete_view import UserDeleteApiView
from tecnologia.usuarios.views.list_view import UserListApiView
from tecnologia.usuarios.views.update_view import UserUpdateApiView

urlpatterns = [
    path("", UserListApiView.as_view(), name="list"),
    path("create/", UserCreateApiView.as_view(), name="create"),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDeleteApiView.as_view(), name="delete"),
]
