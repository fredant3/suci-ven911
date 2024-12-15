from django.core.exceptions import ObjectDoesNotExist


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

    def create(self, data):
        data = {k: v for k, v in data.items() if k != "csrfmiddlewaretoken"}
        entity = self.entity(**data)
        entity.save()
        return entity

    def update(self, entity, payload):
        print(entity)
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
