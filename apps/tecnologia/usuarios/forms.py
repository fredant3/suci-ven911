from django import forms
from users.auth.models import User
from helpers.FormBase import FormBase
from helpers.models import BOOLEAN_CHOICES


class UserForm(FormBase):
    is_active = forms.ChoiceField(
        choices=BOOLEAN_CHOICES,
        widget=forms.Select,
        label="Activo",
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
            "password": "Contraseña",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Usuario"}),
            "dni": forms.TextInput(attrs={"placeholder": "DNI"}),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Contraseña", "class": "input__input"}
            ),
        }
