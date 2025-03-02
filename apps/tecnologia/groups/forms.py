from django import forms
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from helpers.FormBase import FormBase


class GrupoPermisosForm(FormBase):
    container_class = "inputContainer--inline"
    input_class = "input--width"

    class Meta:
        model = Group
        fields = ["name", "permissions"]
        labels = {
            "name": "Nombre del Grupo",
            "permissions": "Permisos",
        }
        widgets = {
            "permissions": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["permissions"].choices = self.get_grouped_permissions()

    def get_grouped_permissions(self):
        # Agrupar permisos por app_label
        permissions = Permission.objects.select_related("content_type").all()
        groups = {}

        for perm in permissions:
            app_label = perm.content_type.app_label
            if app_label not in groups:
                groups[app_label] = []
            groups[app_label].append(
                (perm.id, f"{perm.content_type.name} - {perm.name}")
            )

        # Crear opciones agrupadas
        grouped_choices = []
        for app_label, perms in groups.items():
            grouped_choices.append((app_label.capitalize(), perms))

        return grouped_choices
