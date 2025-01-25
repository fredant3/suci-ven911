from django import forms
from .models import Reglamento

class ReglamentoForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Reglamento
        fields = [
            "name",
            "file",
            "user",
            "date",
            "progre",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]