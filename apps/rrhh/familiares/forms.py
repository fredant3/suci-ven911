from django import forms

from .models import Familiar
from helpers.FormBase import FormBase


class FamiliarForm(FormBase):
    class Meta:
        model = Familiar
        fields = (
            "camisa",
            "pantalon",
            "zapato",
            "personal",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
