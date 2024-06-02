from django import forms
from django.forms import ModelForm
from .models import *
from presupuesto.models import Proyecto, Acciones, Cedente, Receptor, Asignacion

# FORMULARIO DE PRESUPUESTO - PROYECTO
class ProyectoForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Proyecto
        fields = ('id', 'nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE ACTUALIZACIÓN DE PRESUPUESTO
class ProyectoEForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Proyecto
        fields = ('id','nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')
# FORMULARIO DE PRESUPUESTO - PROYECTO
class ProyectoForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Proyecto
        fields = ('id', 'nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE ACTUALIZACIÓN DE PRESUPUESTO
class ProyectoEForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Proyecto
        fields = ('id','nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE PRESUPUESTO - PROYECTO
class AccionesForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Acciones
        fields = ('id', 'nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE ACTUALIZACIÓN DE PRESUPUESTO
class AccionesEForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Acciones
        fields = ('id','nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE ASIGNACION
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ('id', 'nombredir', 'presuasig', 'objeanual', 'numpartida')

# FORMULARIO DE ASIGNACION
class AsignacionUForm(ModelForm):
    class Meta:
        model = Asignacion
        fields = ('id', 'nombredir', 'presuasig', 'objeanual', 'numpartida',)

# FORMULARIO DE CEDENTE
class CedenteForm(forms.ModelForm):
   class Meta:
        model = Cedente
        fields = ('idc', 'partidac', 'generalc', 'espefc', 'subespefc', 'denomc', 'presuacorc', 'caufechac', 'dispc', 'montocc', 'saldofc', 'direccionc')

# FORMULARIO DE ACTUALIZACIÓN VEHÍCULOS
class CedenteUForm(forms.ModelForm):
    class Meta:
        model = Cedente
        fields = ('idc', 'partidac', 'generalc', 'espefc', 'subespefc', 'denomc', 'presuacorc', 'caufechac', 'dispc', 'montocc', 'saldofc', 'direccionc')

# FORMULARIO DE CEDENTE
class ReceptorForm(forms.ModelForm):
   class Meta:
        model = Receptor
        fields = ('idr', 'partidar', 'generalr', 'espefr', 'subespefr', 'denomr', 'presuacorr', 'caufechar', 'dispr', 'montocr', 'saldofr', 'direccionr')

# FORMULARIO DE ACTUALIZACIÓN VEHÍCULOS
class ReceptorUForm(forms.ModelForm):
    class Meta:
        model = Receptor
        fields = ('idr', 'partidar', 'generalr', 'espefr', 'subespefr', 'denomr', 'presuacorr', 'caufechar', 'dispr', 'montocr', 'saldofr', 'direccionr')

# FORMULARIO DE PRESUPUESTO - PROYECTO
class AccionesForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Acciones
        fields = ('id', 'nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE ACTUALIZACIÓN DE PRESUPUESTO
class AccionesEForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Acciones
        fields = ('id','nombrep', 'fechai', 'fechac', 'situacionp', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE ASIGNACION
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ('id', 'nombredir', 'presuasig', 'objeanual', 'numpartida')

# FORMULARIO DE ASIGNACION
class AsignacionUForm(ModelForm):
    class Meta:
        model = Asignacion
        fields = ('id', 'nombredir', 'presuasig', 'objeanual', 'numpartida',)

# FORMULARIO DE CEDENTE
class CedenteForm(forms.ModelForm):
   class Meta:
        model = Cedente
        fields = ('idc', 'partidac', 'generalc', 'espefc', 'subespefc', 'denomc', 'presuacorc', 'caufechac', 'dispc', 'montocc', 'saldofc', 'direccionc')

# FORMULARIO DE ACTUALIZACIÓN VEHÍCULOS
class CedenteUForm(forms.ModelForm):
    class Meta:
        model = Cedente
        fields = ('idc', 'partidac', 'generalc', 'espefc', 'subespefc', 'denomc', 'presuacorc', 'caufechac', 'dispc', 'montocc', 'saldofc', 'direccionc')

# FORMULARIO DE CEDENTE
class ReceptorForm(forms.ModelForm):
   class Meta:
        model = Receptor
        fields = ('idr', 'partidar', 'generalr', 'espefr', 'subespefr', 'denomr', 'presuacorr', 'caufechar', 'dispr', 'montocr', 'saldofr', 'direccionr')

# FORMULARIO DE ACTUALIZACIÓN VEHÍCULOS
class ReceptorUForm(forms.ModelForm):
    class Meta:
        model = Receptor
        fields = ('idr', 'partidar', 'generalr', 'espefr', 'subespefr', 'denomr', 'presuacorr', 'caufechar', 'dispr', 'montocr', 'saldofr', 'direccionr')
