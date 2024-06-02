from django import forms
from django.forms import ModelForm
from .models import *
from .models import Usuarios, Departamentos, Sedes

# FORMULARIO DE CREACIÓN DE USUARIOS - ADMIN
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('username', 'password','correo', 'nombre', 'apellido', 'tipo', 'departamento', 'sede', 'estado')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# FORMULARIO DE ACTUALIZACIÓN DE USUARIOS - ADMIN
class UsuarioAForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('username', 'password','correo', 'nombre', 'apellido', 'tipo', 'departamento', 'sede', 'estado')

# FORMULARIO DE ACTUALIZACIÓN DE PASSWORD USUARIOS - ADMIN
class UsuariosPForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('password',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# FORMULARIO DE CREACIÓN DE DEPARTAMENTOS - ADMIN
class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ('departamento', 'estado')

# FORMULARIO DE ACTUALIZACIÓN DE DEPARTAMENTOS - ADMIN
class DepartamentosEForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ('departamento', 'estado')
        
# FORMULARIO DE CREACIÓN DE SEDES - ADMIN
class SedesForm(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ('direccion', 'municipio','estado')

# FORMULARIO DE ACTUALIZACIÓN DE SEDES - ADMIN
class SedesEForm(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ('direccion', 'municipio','estado')
        