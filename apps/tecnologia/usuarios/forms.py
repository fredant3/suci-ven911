from django.forms import BooleanField, CheckboxInput
from users.auth.models import User
from helpers.FormBase import FormBase
from django import forms
from apps.rrhh.models import Empleado


class UserForm(FormBase):
    is_active = BooleanField(
        required=False,
        widget=CheckboxInput(attrs={"value": "False"}),
    )

    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.all(),
        label="Empleado",
        widget=forms.Select(
            attrs={
                "class": "select-with-search",
                "data-placeholder": "Buscar empleado...",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "dni",
            "is_active",
            "password",
        )
        labels = {
            "username": "Usuario",
            "dni": "DNI",
            "is_active": "Activo",
            "password": "Contraseña",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Usuario"}),
            "dni": forms.TextInput(attrs={"placeholder": "DNI"}),
            "is_active": forms.CheckboxInput(attrs={"value": "False"}),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Contraseña", "class": "input__input"}
            ),
        }
