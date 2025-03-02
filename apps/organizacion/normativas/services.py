from helpers.CrudMixin import CrudService

from organizacion.normativas.repositories import NormativaRepository
from django.db.models import Q


class NormativaService(CrudService):
    def __init__(self):
        self.repository = NormativaRepository()

    def media(self, data, media):
        custom_folder = "normativas"
        if media["file"]:
            data["file"] = self.repository.media(media["file"], custom_folder)
        return data

    def remove_media(self, data):
        read = self.reader(data.id)
        file = read.file
        if file:
            self.repository.remove_media(file.path)

    def criteria(self, search):
        query = Q()

        if search:
            query &= Q(name__icontains=search) | Q(progre__icontains=search)

        return query
