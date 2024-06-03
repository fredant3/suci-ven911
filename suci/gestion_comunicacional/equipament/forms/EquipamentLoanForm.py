from django.forms import ModelForm
from gestion_comunicacional.equipament.entities.EquipamentLoanEntity import (
    EquipamentLoanEntity,
)


class EquipamentLoanForm(ModelForm):
    class Meta:
        model = EquipamentLoanEntity
        fields = (
            "equipment",
            "department",
            "loan_date",
            "return_date",
        )
