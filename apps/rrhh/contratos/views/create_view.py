from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from formtools.wizard.views import SessionWizardView
from rrhh.contratos.forms import ContratoForm
from rrhh.empleados.forms import EmpleadoForm
from rrhh.educaciones.forms import EducacionForm
from rrhh.familiares.forms import FamiliarForm
from rrhh.dotaciones.forms import DotacionForm

# rrhh.sueldos.forms import SueldoForm

from templates.sneat import TemplateLayout
from django.http import HttpResponseRedirect

from ..services import ContratoService

from rrhh.empleados.models import Empleado
from rrhh.contratos.models import Contrato
from rrhh.educaciones.models import Educacion
from rrhh.familiares.models import Familiar
from rrhh.dotaciones.models import Dotacion

# from sueldos.models import Sueldo


class ContratoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "rrhh.contratos.agregar_contrato"
    form_class = ContratoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Contratos"
        context["titleForm"] = "Añadir una contrato nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("contratos:list")
        context["urlForm"] = reverse_lazy("api_contratos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ContratoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "rrhh.contratos.agregar_contrato"
    form_class = [
        EmpleadoForm,
        EducacionForm,
        FamiliarForm,
        DotacionForm,
        ContratoForm,
        # SueldoForm, no guarda sueldo, modelo mal organizado
    ]


class rrhhWizardView(SessionWizardView):
    template_name = "widzard/indexrrhh.html"
    form_list = [
        ("empleado", EmpleadoForm),
        ("educacion", EducacionForm),
        ("familiar", FamiliarForm),
        ("dotacion", DotacionForm),
        ("contrato", ContratoForm),
        # ("sueldo", SueldoForm),
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Contrato"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "rrhh"
        context["submodule"] = "Contrato"
        return TemplateLayout.init(self, context)

    def done(self, form_list, form_dict, **kwargs):
        # Obtener datos de todos los formularios
        datos_empleado = form_dict["empleado"].cleaned_data
        datos_educacion = form_dict["educacion"].cleaned_data
        datos_familiar = form_dict["familiar"].cleaned_data
        datos_dotacion = form_dict["dotacion"].cleaned_data
        datos_contrato = form_dict["contrato"].cleaned_data

        # 1. Crear y guardar el empleado
        empleado = Empleado.objects.create(
            **datos_empleado
        )  # Usa create para obtener la instancia

        # 2. Asignar el empleado a los demás modelos
        educacion = Educacion.objects.create(**datos_educacion, empleado=empleado)
        familiar = Familiar.objects.create(**datos_familiar, empleado=empleado)
        dotacion = Dotacion.objects.create(**datos_dotacion, empleado=empleado)
        contrato = Contrato.objects.create(**datos_contrato, empleado=empleado)

        # Redirigir a la lista de contratos
        return HttpResponseRedirect("/gestion-humana/contratos")


# def __init__(self):
# self.service = ContratoService()
