from django.contrib.auth.models import Group, Permission


class Roles:
    def execute(self):
        Group.objects.get_or_create(name="admin")
        adminGroup = Group.objects.get(name="admin")
        permissionsAdmin = []

        for module in [
            # "users", TODO: Pendiente
            # ADMINISTRACION,
            "asignacion",
            "averia",
            "compra",
            "departamento",
            "articulo",
            "sede"
            # ASESORIA,
            "denuncia",
            "registro filmico",
            # EMERGENCIA
            "incidencia",
            "organismo",
            "emergencia",
            # ORGANIZACION
            "normativa",
            "reglamento",
            # PLANIFICACION
            "actividad",
            "infraestructura",
            "llamada",
            "objetivo",
            "transporte",
            # POTENCIA
            "incidencia",
            "uri",
            # PRESUPUESTO
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
            # SEGURIDAD
            "entrada",
            "gestione",
            "salida",
            "vehiculo",
            # TECNOLOGIA
            "grupos",
            "usuarios",
        ]:
            # LOS PERMISOS
            list = Permission.objects.get(codename=f"listar_{module}")
            read = Permission.objects.get(codename=f"ver_{module}")
            add = Permission.objects.get(codename=f"agregar_{module}")
            change = Permission.objects.get(codename=f"editar_{module}")
            delete = Permission.objects.get(codename=f"eliminar_{module}")
            excel = Permission.objects.get(codename=f"exel_{module}")

            Group.objects.get_or_create(name=f"{module} director")
            Group.objects.get_or_create(name=f"{module} gerente")
            Group.objects.get_or_create(name=f"{module} supervisor")
            Group.objects.get_or_create(name=f"{module} analista")

            director = Group.objects.get(name=f"{module} director")
            permissionsDirector = []
            permissionsDirector.append(list.id)
            permissionsDirector.append(add.id)
            permissionsDirector.append(read.id)
            permissionsDirector.append(change.id)
            permissionsDirector.append(delete.id)
            permissionsDirector.append(excel.id)
            director.permissions.set(permissionsDirector)

            gerente = Group.objects.get(name=f"{module} coordinador")
            permissionsGerente = []
            permissionsGerente.append(list.id)
            permissionsGerente.append(add.id)
            permissionsGerente.append(read.id)
            permissionsGerente.append(change.id)
            permissionsGerente.append(delete.id)
            permissionsDirector.append(excel.id)
            gerente.permissions.set(permissionsGerente)

            supervisor = Group.objects.get(name=f"{module} supervisor")
            permissionsSupervisor = []
            permissionsSupervisor.append(list.id)
            permissionsSupervisor.append(add.id)
            permissionsSupervisor.append(read.id)
            permissionsGerente.append(change.id)
            supervisor.permissions.set(permissionsSupervisor)

            analista = Group.objects.get(name=f"{module} analista")
            permissionsAnalista = []
            permissionsAnalista.append(list.id)
            permissionsSupervisor.append(add.id)
            permissionsAnalista.append(read.id)
            analista.permissions.set(permissionsAnalista)

            permissionsAdmin.append(list.id)
            permissionsAdmin.append(read.id)
            permissionsAdmin.append(add.id)
            permissionsAdmin.append(change.id)
            permissionsAdmin.append(delete.id)

        adminGroup.permissions.set(permissionsAdmin)

        print(f"Grupo {self.adminGroup.name} creado exitosamente.")
