from apps.usuario.models import Usuario
from django import forms
from django.forms import ModelForm


class FormularioUsuario(ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese su contraseña...",
                "id": "password1",
                "required": "required",
            }
        ),
    )

    password2 = forms.CharField(
        label="Contraseña de Confirmación",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese nuevamente su contraseña...",
                "id": "password2",
                "required": "required",
            }
        ),
    )

    class Meta:
        model = Usuario
        fields = ("email", "username", "nombres", "apellidos", "rol")
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Correo Electrónico",
                }
            ),
            "nombres": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese su nombre",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese sus apellidos",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese su nombre de usuario",
                }
            ),
            "rol": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
