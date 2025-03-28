from django.forms import BooleanField, CheckboxInput
from users.auth.models import User
from helpers.FormBase import FormBase
from django import forms


class UserForm(FormBase):
    is_active = BooleanField(
        required=False,
        widget=CheckboxInput(attrs={"value": "False"}),
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
