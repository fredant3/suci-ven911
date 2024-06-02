from django import forms
from django.forms import ModelForm
from .models import *
from organizacion.models import Reglamentos, Normativas


# FORMULARIO DE REGLAMENTOS
class ReglamentsForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Reglamentos
        fields = ("name", "user", "date", "progre", "estado", "file")


# FORMULARIO DE ACTUALIZACIÓN DE REGLAMENTOS
class ReglamentsUForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Reglamentos
        fields = ("name", "user", "date", "progre", "estado")


# FORMULARIO DE ACTUALIZACIÓN DE ARCHIVO REGLAMENTOS
class ReglamentsUFForm(forms.ModelForm):
    class Meta:
        model = Reglamentos
        fields = ("file",)


# FORMULARIO DE NORMATIVAS
class NormativasForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Normativas
        fields = ("name", "user", "date", "progre", "estado", "file")


# FORMULARIO DE ACTUALIZACIÓN NORMATIVAS
class NormativasUForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Normativas
        fields = ("name", "user", "date", "progre", "estado")


# FORMULARIO DE ACTUALIZACIÓN DE ARCHIVOS NORMATIVAS
class NormativasUFForm(forms.ModelForm):
    class Meta:
        model = Normativas
        fields = ("file",)
