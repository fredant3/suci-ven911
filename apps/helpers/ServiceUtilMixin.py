from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class ServiceUtilMixin:
    def relationship(self, payload, *arg, **kwargs):
        return payload

    def prepare_data(self, request, *arg, **kwargs):
        data = request.POST.copy()

        user = request.user
        if data.get("id") is None:
            data["created_by"] = user.username
        data["updated_by"] = user.username

        return self.relationship(data, *arg, **kwargs)

    def paginate(self, data, start, length, draw):
        entities = data[start : start + length]
        paginator = Paginator(entities, length)

        try:
            items = paginator.page(draw).object_list
        except PageNotAnInteger:
            items = paginator.page(draw).object_list
        except EmptyPage:
            items = paginator.page(paginator.num_pages).object_list
        return items

    def response(self, entities, start, length, draw):
        response = {}
        data = []
        payload = self.paginate(entities, start, length, draw)
        for item in payload:
            data.append(item)

        records_total = entities.count()

        response["draw"] = draw
        response["entities"] = data
        response["recordsTotal"] = records_total
        response["recordsFiltered"] = records_total
        return response

    class Meta:
        abstract = True
