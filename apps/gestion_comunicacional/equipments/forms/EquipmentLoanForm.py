from gestion_comunicacional.equipments.entities.EquipmentLoanEntity import EquipmentLoanEntity

from django.forms import ModelForm


class EquipmentLoanForm(ModelForm):
    class Meta:
        model = EquipmentLoanEntity
        fields = (
            "equipments",
            "department",
            "loan_date",
            "return_date",
        )
