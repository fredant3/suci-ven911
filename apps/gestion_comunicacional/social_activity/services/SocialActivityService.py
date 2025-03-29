from gestion_comunicacional.social_activity.repositories.SocialActivityRepository import SocialActivityRepository
from index.mixins.CrudMixin import CrudService

from django.db.models import Q


class SocialActivityService(CrudService):
    def __init__(self):
        self.repository = SocialActivityRepository()

    def getAll(self, draw, start, length, search=None, select=("")):
        query = None
        if search:
            query = Q()
            for column in ["id", "activity_type", "reason"]:
                query |= Q(**{f"{column}__icontains": search})

        return super().getAll(draw, start, length, query, select)
