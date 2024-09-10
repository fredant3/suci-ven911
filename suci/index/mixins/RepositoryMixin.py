from index.mixins.ServiceUtilMixin import ServiceUtilMixin

from django.core.exceptions import ObjectDoesNotExist, ValidationError


class Repository:
    def getAll(self, select):
        return self.entity.objects.all().values(*select)

    def getFilter(self, criteria, select):
        return self.entity.objects.filter(criteria).values(*select)

    def getById(self, id, select):
        entity = self.entity.objects.get(pk=id).values(*select)

        if entity is None:
            raise ObjectDoesNotExist("No %s matches the given query." % self.entity.__name__)

        return entity

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
