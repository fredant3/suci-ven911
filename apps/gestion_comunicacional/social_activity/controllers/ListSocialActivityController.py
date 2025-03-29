import json

from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService
from index.mixins.CheckPermisosMixin import CheckPermisosMixin
from index.mixins.ControllerMixin import ListController
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView


class ListSocialActivityView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    template_name = "gc/social-activity/listing.html"
    permission_required = SocialActivityEntity.VIEW_SOCIAL_ACTIVITY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sa_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sa_module_name"
        context["createBtn"] = "gc_sa_title_btn_add"
        context["createUrl"] = reverse_lazy("gc:sa:create-activity")
        context["listUrl"] = reverse_lazy("gc:sa:api-listing-activity")
        context["updateUrl"] = reverse_lazy("gc:sa:updater-activity", args=[0])
        context["deleteUrl"] = reverse_lazy("gc:sa:destroyer-activity", args=[0])
        columns = [
            {"data": "id", "name": "id", "title": "ID", "orderable": "true", "searchable": "true"},
            {"data": "date", "name": "date", "title": "Fecha y hora", "orderable": "false", "searchable": "false"},
            {
                "data": "activity_type",
                "name": "activity_type",
                "title": "Tipo de Actividad",
                "orderable": "true",
                "searchable": "false",
            },
            # {"data": "location", "name": "location", "title": "Ubicacion", "orderable": "false", "searchable": "false"},
            {"data": "reason", "name": "reason", "title": "Motivo", "orderable": "false", "searchable": "true"},
            # {
            #     "data": "description",
            #     "name": "description",
            #     "title": "Descripcion",
            #     "orderable": "false",
            #     "searchable": "false",
            # },
            {
                "data": "beneficiaries",
                "name": "beneficiaries",
                "title": "Beneficiarios",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "title": "Acciones",
            },
        ]
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)


class ListSocialActivity(ListController, CheckPermisosMixin):
    permission_required = SocialActivityEntity.VIEW_SOCIAL_ACTIVITY

    def __init__(self):
        self.service = SocialActivityService()
