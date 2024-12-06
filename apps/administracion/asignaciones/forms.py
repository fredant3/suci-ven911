from administracion.asignaciones.models import Asignacion
from administracion.inventario.models import Articulo
from django import forms


class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "articulo": forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super(AsignacionForm, self).__init__(*args, **kwargs)
        self.fields["articulo"].queryset = Articulo.objects.filter(asignado=False)


class AsignacionUpdateForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo (Solo lectura)",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "articulo": forms.Select(
                attrs={"style": "pointer-events: none;", "readonly": "readonly"}
            ),
        }
