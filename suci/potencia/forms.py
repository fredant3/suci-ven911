from django import forms
from django.forms import ModelForm
from .models import *
from potencia.models import Incidencias

class FormularioIncidencias(forms.Form):
    class Meta:
        model = Incidencias
        fields = '__all__'