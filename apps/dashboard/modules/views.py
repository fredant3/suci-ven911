from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from templates.sneat import TemplateLayout


class Modules(LoginRequiredMixin, TemplateView):
    login_url = "auth:login"
    template_name = "public/modules/index.html"

    PERMISSIONS_ASESORIA = (
        "asesoria.agregar_denuncia",
        "asesoria.editar_denuncia",
        "asesoria.eliminar_denuncia",
        "asesoria.exel_denuncia",
        "asesoria.listar_denuncia",
        "asesoria.ver_denuncia",
        "asesoria.agregar_registro_filmico",
        "asesoria.editar_registro_filmico",
        "asesoria.eliminar_registro_filmico",
        "asesoria.exel_registro_filmico",
        "asesoria.listar_registro_filmico",
        "asesoria.ver_registro_filmico",
    )

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["modules"] = [
            {
                "title": "Asesoría Jurídica",
                "url": "asesoria",
                "image": "img/modules/asesoria_juridica.png",
                "user_has_access": any(
                    self.request.user.has_perm(perm)
                    for perm in self.PERMISSIONS_ASESORIA
                )
                or self.request.user.is_superuser,
            },
            {
                "title": "Gestión Humana",
                "url": "gestion_humana",
                "image": "img/modules/gestion_humana.png",
                "user_has_access": self.request.user.is_superuser
                or any(
                    self.request.user.has_perm(perm)
                    for perm in self.PERMISSIONS_ASESORIA
                ),
            },
            {
                "title": "Gestión Administrativa",
                "url": "administracion",
                "image": "img/modules/gestion_administrativa.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Unidad de Respuesta Inmediata",
                "url": "uri:list",
                "image": "img/modules/ambulancias.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Potencia",
                "url": "potencia",
                "image": "img/modules/incidente.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Organización",
                "url": "organizacion",
                "image": "img/modules/organizacion.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Presupuestos",
                "url": "presupuesto",
                "image": "img/modules/presupuesto.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Planificación",
                "url": "planificacion",
                "image": "img/modules/planificacion.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Protección y Seguridad Integral",
                "url": "seguridad",
                "image": "img/modules/seguridad.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Biblioteca de Manuales",
                "url": "bibliotecas",
                "image": "img/modules/biblioteca.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Operaciones",
                "url": "operaciones",
                "image": "img/modules/ambulancia.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Tecnología Comunicación e Información",
                "url": "tecnologia",
                "image": "img/modules/tecnologia.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
            {
                "title": "Gestion Comunicacional",
                "url": "gc_info",
                "image": "img/modules/GC_icon.png",
                "user_has_access": self.request.user.is_superuser,
                # or any(
                #     self.request.user.has_perm(perm)
                #     for perm in self.PERMISSIONS_ASESORIA
                # ),
            },
        ]
        return context
