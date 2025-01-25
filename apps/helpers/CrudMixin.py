from django.core.exceptions import ValidationError

from .ServiceUtilMixin import ServiceUtilMixin


class CrudService(ServiceUtilMixin):
    select = ""

    def criteria(self, search):
        return search

    def getAll(
        self, draw, start, length, search=None, orderBy=None, orderAsc=None, select=("")
    ):
        select = select if select else self.select
        if search is None:
            entities = self.repository.getAll(select, orderBy, orderAsc)
        else:
            search = self.criteria(search)
            entities = self.repository.getFilter(search, select, orderBy, orderAsc)

        return self.response(entities, start, length, draw)

    def creator(self, form, request, *arg, **kwargs):
        data = self.prepare_data(request, *arg, **kwargs)
        if form.is_valid():
            form.clean()
            data = self.before_create(data)
            data = self.media(data, request.FILES)
            return self.repository.create(data)
        raise ValidationError(form.errors.as_json())

    def reader(self, id, select=("")):
        return self.repository.getById(id, select)

    def updater(self, entity, payload):
        if payload.is_valid():
            payload.clean()
            self.before_update(entity, payload)
            return self.repository.update(entity, payload)
        raise ValidationError(payload.errors.as_json())

    def destroyer(self, payload):
        self.remove_media(payload)
        return self.repository.delete(payload)

    class Meta:
        abstract = True
