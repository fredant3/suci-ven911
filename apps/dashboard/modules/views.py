from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import Permisos

from templates.sneat import TemplateLayout


class Modules(LoginRequiredMixin, TemplateView):
    login_url = "auth:login"
    template_name = "public/modules/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["modules"] = [
            {
                "title": "Asesoría Jurídica",
                "url": "asesoria",
                "image": "img/modules/asesoria_juridica.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "asesoria"
                ),
            },
            {
                "title": "Gestión Humana",
                "url": "gestion_humana",
                "image": "img/modules/gestion_humana.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "gestion_humana"
                ),
            },
            {
                "title": "Gestión Administrativa",
                "url": "administracion",
                "image": "img/modules/gestion_administrativa.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "administracion"
                ),
            },
            {
                "title": "Unidad de Respuesta Inmediata",
                "url": "uri:list",
                "image": "img/modules/ambulancias.png",
                "user_has_access": Permisos.check_permissions(self.request.user, "uri"),
            },
            {
                "title": "Potencia",
                "url": "potencia",
                "image": "img/modules/incidente.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "potencia"
                ),
            },
            {
                "title": "Organización",
                "url": "organizacion",
                "image": "img/modules/organizacion.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "no implementado"
                ),
            },
            {
                "title": "Presupuestos",
                "url": "presupuesto",
                "image": "img/modules/presupuesto.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "asesoria"
                ),
            },
            {
                "title": "Planificación",
                "url": "planificacion",
                "image": "img/modules/planificacion.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "planificacion"
                ),
            },
            {
                "title": "Protección y Seguridad Integral",
                "url": "seguridad",
                "image": "img/modules/seguridad.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "seguridad"
                ),
            },
            {
                "title": "Biblioteca de Manuales",
                "url": "bibliotecas",
                "image": "img/modules/biblioteca.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "no implementado"
                ),
            },
            {
                "title": "Operaciones",
                "url": "operaciones",
                "image": "img/modules/ambulancia.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "operaciones"
                ),
            },
            {
                "title": "Tecnología Comunicación e Información",
                "url": "tecnologia",
                "image": "img/modules/tecnologia.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "no implementado"
                ),
            },
            {
                "title": "Gestion Comunicacional",
                "url": "gc_info",
                "image": "img/modules/GC_icon.png",
                "user_has_access": Permisos.check_permissions(
                    self.request.user, "asesoria"
                ),
            },
        ]
        return context
