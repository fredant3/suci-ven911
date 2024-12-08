from django.core.management.base import BaseCommand
from faker import Faker
from helpers.management.commands.seed.administracion._Departamento import (
    DepartamentoFaker,
)
from helpers.management.commands.seed.administracion._Inventario import ArticleFake
from helpers.management.commands.seed.administracion._Sede import SedesFaker
from helpers.management.commands.seed.users._UserFaker import UserFaker


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker("es_ES")

        admin = UserFaker.admin_user()
        guest = UserFaker.guest_user()
        other = UserFaker.other_user()

        ArticleFake.type_article()
        ArticleFake.article(fake)

        SedesFaker.add_sedes(fake)
        DepartamentoFaker.add_departamentos(fake)
