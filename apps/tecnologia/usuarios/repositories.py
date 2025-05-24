from helpers.RepositoryMixin import Repository
from users.auth.models import User
from rrhh.empleados.models import Empleado
from django.db.models import Q


class UserRepository(Repository):
    def __init__(self):
        self.entity = User

    def get_all_with_related(self, search=None):
        empleados_con_usuarios = (
            Empleado.objects.filter(usuario__isnull=False)
            .select_related("usuario")
            .prefetch_related("contratos")
        )
        users = self.entity.objects.all()

        if search:
            empleados_con_usuarios = empleados_con_usuarios.filter(
                Q(nombres__icontains=search)
                | Q(apellidos__icontains=search)
                | Q(cedula__icontains=search)
                | Q(usuario__username__icontains=search)
            )
            users = users.filter(
                Q(username__icontains=search)
                | Q(dni__icontains=search)
                | Q(empleado__nombres__icontains=search)
                | Q(empleado__apellidos__icontains=search)
                | Q(empleado__cedula__icontains=search)
            )

        empleados_map = {emp.usuario_id: emp for emp in empleados_con_usuarios}

        return users, empleados_map
