from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from templates.sneat import TemplateLayout


class Modules(LoginRequiredMixin, TemplateView):
    login_url = "auth:login"
    template_name = "public/modules/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["modules"] = [
            # {
            #     "title": "Admin",
            #     "url": "modules:index",
            #     "image": "img/gestion_administrativa.png",
            # },
            {
                "title": "Asesoría Jurídica",
                "url": "asesoria",
                "image": "img/gestion_administrativa.png",
            },
            {
                "title": "Biblioteca de Manuales",
                "url": "bibliotecas",
                "image": "img/biblioteca.png",
            },
            {
                "title": "Emergencias",
                "url": "emergencias:list",
                "image": "img/cuadrantes_de_paz.png",
            },
            {
                "title": "Planificación",
                "url": "planificacion",
                "image": "img/planificacion.png",
            },
            {
                "title": "Presupuestos",
                "url": "presupuesto",
                "image": "img/presupuesto.png",
            },
            {
                "title": "Gestión Administrativa",
                "url": "administracion",
                "image": "img/gestion_administrativa.png",
            },
            # {"title": "Operaciones Cuadrantes de Paz", "url": "gc:info", "image": "img/cuadrantes_de_paz.png"},
            {
                "title": "Gestión Humana",
                "url": "gestion_humana",
                "image": "img/gestion_humana.png",
            },
            # {"title": "Tecnología Comunicación e Información", "url": "gc:info", "image": "img/tecnologia.png"},
            # {"title": "Unidad de Respuesta Inmediata", "url": "gc:info", "image": "img/ambulancia.png"},
            # {"title": "Potencia", "url": "gc:info", "image": "img/incidente.png"},
            {
                "title": "Organización",
                "url": "organizacion",
                "image": "img/organizacion.png",
            },
            # {"title": "Presupuesto", "url": "gc:info", "image": "img/presupuesto.png"},
            # {"title": "Seguridad Integral", "url": "gc:info", "image": "img/seguridad.png"},
            # {"title": "Admin", "url": "gc:info", "image": "img/admin.png"},
        ]
        return context
