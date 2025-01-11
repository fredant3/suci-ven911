from django.core.exceptions import ObjectDoesNotExist
import os
from pathlib import Path


class Repository:
    def after_get_all(self, entities):
        return entities

    def getAll(self, select, orderBy, orderAsc):
        orderBy = orderBy if orderBy else "id"
        order = orderBy if orderAsc == "asc" else "-" + orderBy
        entities = self.entity.objects.all().order_by(order).values(*select)
        return self.after_get_all(entities)

    def getFilter(self, criteria, select="", orderBy="id", orderAsc="-"):
        orderBy = orderBy if orderBy else "id"
        order = orderBy if orderAsc == "asc" else "-" + orderBy
        entities = self.entity.objects.filter(criteria).order_by(order).values(*select)
        return self.after_get_all(entities)

    def getById(self, id, select=""):
        # entity = self.entity.objects.get(pk=id).values(*select)
        entity = self.entity.objects.get(pk=id)

        if entity is None:
            raise ObjectDoesNotExist(
                "No %s matches the given query." % self.entity.__name__
            )

        return entity

    def media(self, file):
        path = self.media_folder(file)
        self.seve_media(path, file)

    def media_folder(self, file):
        file_extension = Path(file.name).suffix.lower()

        if file_extension in [".jpg", ".png", ".gif", ".bmp"]:
            folder = "images"
        elif file_extension == ".pdf":
            folder = "pdfs"
        elif file_extension in [".mp4", ".avi", ".mov", ".mkv"]:
            folder = "videos"
        else:
            raise ObjectDoesNotExist(
                "El archivo %s, tiene un formato no soportado: ." % file.name
            )

        return self.ensure_folder(folder, file)

    def ensure_folder(self, folder, file):
        file_path = os.path.join("media", folder, file.name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        return file_path

    def seve_media(self, path, file):
        with open(path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    def create(self, data):
        data = {k: v for k, v in data.items() if k != "csrfmiddlewaretoken"}
        entity = self.entity(**data)
        entity.save()
        return entity

    def update(self, entity, payload):
        for field in payload.fields:
            if hasattr(entity, field):
                setattr(entity, field, payload.cleaned_data[field])
        entity.save()
        return entity

    def delete(self, payload):
        return payload.delete()

    def destroy(self, payload):
        return payload.delete()

    class Meta:
        abstract = True
