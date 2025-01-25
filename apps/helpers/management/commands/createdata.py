from django.core.management.base import BaseCommand
from faker import Faker
from helpers.management.commands.seed.administracion._Departamento import (
    DepartamentoFaker,
)
from helpers.management.commands.seed.administracion._Inventario import ArticleFake
from helpers.management.commands.seed.administracion._Sede import SedesFaker
from helpers.management.commands.seed.administracion._Averia import AveriaFake
from helpers.management.commands.seed.potencia._Incidencias import IncidenciaFake
from helpers.management.commands.seed.users._UserFaker import UserFaker

# from helpers.management.commands.seed.rrhh._TipoSueldoFake import TipoSueldoFake


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker("es_ES")

        UserFaker.admin_user()
        UserFaker.guest_user()
        UserFaker.other_user()

        ArticleFake.type_article()
        ArticleFake.article(fake)

        SedesFaker.add_sedes(fake)
        DepartamentoFaker.add_departamentos(fake)
        IncidenciaFake.tipo_incidencia()
        AveriaFake.tipo_averia()

        # Gestion Humana (RRHH)
        # TipoSueldoFake.tipos_sueldos(fake)
