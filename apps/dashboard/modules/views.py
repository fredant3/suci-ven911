from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from templates.sneat import TemplateLayout


class Modules(LoginRequiredMixin, TemplateView):
    login_url = "auth:login"
    template_name = "public/modules/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["modules"] = [
            {
                "title": "Operaciones Cuadrantes de Paz (Pendiente)",
                "url": "asesoria",
                "image": "img/modules/cuadrantes_de_paz.png",
            },
            {
                "title": "Asesoría Jurídica",
                "url": "asesoria",
                "image": "img/modules/asesoria_juridica.png",
            },
            {
                "title": "Gestión Humana (Pendiente)",
                "url": "tipos_sueldos:list",
                "image": "img/modules/gestion_humana.png",
            },
            {
                "title": "Gestión Administrativa",
                "url": "administracion",
                "image": "img/modules/gestion_administrativa.png",
            },
            {
                "title": "Unidad de Respuesta Inmediata (Pendiente)",
                "url": "uri:list",
                "image": "img/modules/ambulancia.png",
            },
            {
                "title": "Potencia",
                "url": "incidencias:list",
                "image": "img/modules/incidente.png",
            },
            {
                "title": "Organización",
                "url": "organizacion",
                "image": "img/modules/organizacion.png",
            },
            {
                "title": "Presupuestos",
                "url": "presupuesto",
                "image": "img/modules/presupuesto.png",
            },
            {
                "title": "Planificación",
                "url": "planificacion",
                "image": "img/modules/planificacion.png",
            },
            {
                "title": "Protección y Seguridad Integral",
                "url": "seguridad",
                "image": "img/modules/seguridad.png",
            },
            {
                "title": "Biblioteca de Manuales (---)",
                "url": "bibliotecas",
                "image": "img/modules/biblioteca.png",
            },
            {
                "title": "Emergencias",
                "url": "emergencias:list",
                "image": "img/modules/ambulancia.png",
            },
            {
                "title": "Tecnología Comunicación e Información (Pendiente)",
                "url": "asesoria",
                "image": "img/modules/tecnologia.png",
            },
            {
                "title": "Permisos y Usuarios (Pendiente)",
                "url": "asesoria",
                "image": "img/modules/admin.png",
            },
        ]
        return context
