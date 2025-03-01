from django.contrib.auth.models import Group, Permission


def create_group(self):
    Group.objects.get_or_create(name="admin")
    adminGroup = Group.objects.get(name="admin")
    permissionsAdmin = []

    for module in [
        # "users", TODO: Pendiente
        # administracion,
        "asignacion",
        "averia",
        "compra",
        "departamento",
        "articulo",
        "sede"
        # asesoria,
        "denuncia",
        "registroFilmico",
        # Emergencia
        "emergencia",
        # Organizacion
        "normativa",
        "reglamento",
        # planificacion
        "actividad",
        "infraestructura",
        "llamada",
        "objetivo",
        "transporte",
        # potencia
        "incidencia",
        "uri",
        # presupuesto
        "accion",
        "asignacion",
        "cedente",
        "proyecto",
        "receptor",
        # RRHH
        "cargo",
        "contrato",
        "cuenta",
        "dotacion",
        "educacion",
        "empleado",
        "familiares",
        "sueldoEmpleado",
        "tipoEmpleado",
        "tipoSueldo",
        # seguridad
        "entrada",
        "gestione",
        "salida",
        "vehiculo",
    ]:
        # LOS PERMISOS
        list = Permission.objects.get(codename=f"listar_{module}")
        read = Permission.objects.get(codename=f"ver_{module}")
        add = Permission.objects.get(codename=f"agregar_{module}")
        change = Permission.objects.get(codename=f"editar_{module}")
        delete = Permission.objects.get(codename=f"eliminar_{module}")
        excel = Permission.objects.get(codename=f"exel_{module}")

        Group.objects.get_or_create(name=f"{module} gerente")
        Group.objects.get_or_create(name=f"{module} supervisor")
        Group.objects.get_or_create(name=f"{module} analista")

        gerente = Group.objects.get(name=f"{module} gerente")
        permissionsGerente = []
        permissionsGerente.append(list.id)
        permissionsGerente.append(read.id)
        permissionsGerente.append(add.id)
        permissionsGerente.append(change.id)
        permissionsGerente.append(delete.id)
        gerente.permissions.set(permissionsGerente)

        supervisor = Group.objects.get(name=f"{module} supervisor")
        permissionsSupervisor = []
        permissionsSupervisor.append(list.id)
        permissionsSupervisor.append(read.id)
        permissionsSupervisor.append(add.id)
        supervisor.permissions.set(permissionsSupervisor)

        analista = Group.objects.get(name=f"{module} analista")
        permissionsAnalista = []
        permissionsAnalista.append(list.id)
        permissionsAnalista.append(read.id)
        analista.permissions.set(permissionsAnalista)

        permissionsAdmin.append(list.id)
        permissionsAdmin.append(read.id)
        permissionsAdmin.append(add.id)
        permissionsAdmin.append(change.id)
        permissionsAdmin.append(delete.id)

    adminGroup.permissions.set(permissionsAdmin)

    print(f"Grupo {self.adminGroup.name} creado exitosamente.")
