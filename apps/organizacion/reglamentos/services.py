from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import ReglamentoRepository


class ReglamentoService(CrudService):
    def __init__(self):
        self.repository = ReglamentoRepository()

    def getAll(
        self, draw, start, length, search=None, orderBy=None, orderAsc=None, select=("")
    ):
        query = None
        if search:
            query = Q()
            for column in ["id", "name"]:
                query |= Q(**{f"{column}__icontains": search})

        return super().getAll(draw, start, length, query, orderBy, orderAsc, select)

    def media(self, data, media):
        custom_folder = "reglamentos"
        if media["file"]:
            data["file"] = self.repository.media(media["file"], custom_folder)
        return data

    def remove_media(self, data):
        read = self.reader(data.id)
        file = read.file
        if file:
            self.repository.remove_media(file.path)
