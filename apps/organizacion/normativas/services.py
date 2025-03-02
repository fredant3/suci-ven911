from django.conf import settings
from helpers.CrudMixin import CrudService
from organizacion.normativas.repositories import NormativaRepository


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

    def getAll(
        self, draw, start, length, search=None, orderBy=None, orderAsc=None, select=("")
    ):
        select = select if select else self.select
        if search is None:
            entities = self.repository.getAll(select, orderBy, orderAsc)
        else:
            search = self.criteria(search)
            entities = self.repository.getFilter(search, select, orderBy, orderAsc)

        for field in entities:
            if "file" in field:
                url_file = f"{settings.MEDIA_URL}{field['file']}"
                field["file"] = (
                    f'<img src="{url_file}" style="height:50px;width:50px;" />'
                )

        return self.response(entities, start, length, draw)
