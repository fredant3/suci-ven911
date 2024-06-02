from django import forms
from django.forms import ModelForm
from .models import *
from .models import Sexo, EstadoCivil,TallasCamisa, TallasPantalon, TallasZapatos, Grado, TipoPersonal, Cargo, Departamento, Sedes

class FormEstadoC(forms.ModelForm):
    class Meta:
        model = EstadoCivil
        fields = ['estado_civil']

class GeneroFormSexo(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ['sexo']

class FormTallaC(forms.ModelForm):
    class Meta:
        model = TallasCamisa
        fields = ['talla_camisa']

class FormTallaP(forms.ModelForm):
    class Meta:
        model = TallasPantalon
        fields = ['talla_pantalon']

class FormTallaZ(forms.ModelForm):
    class Meta:
        model = TallasZapatos
        fields = ['talla_zapato']

class FormGradoI(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['grado_instruccion']

class FormTipoPersonal(forms.ModelForm):
    class Meta:
        model = TipoPersonal
        fields = ['tipo_personal']

class FormCargo(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['cargo']

class FormDepartamento(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['departamento']

class FormSedes(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ['sede']
