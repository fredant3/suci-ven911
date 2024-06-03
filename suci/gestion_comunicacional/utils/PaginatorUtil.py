from django.core.paginator import EmptyPage, PageNotAnInteger


class PaginatorUtil:
    @staticmethod
    def paginate(paginator, page):
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return items
