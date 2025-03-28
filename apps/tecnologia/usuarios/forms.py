from django.forms import BooleanField, CheckboxInput
from users.auth.models import User
from helpers.FormBase import FormBase


class UserForm(FormBase):        
    is_active = BooleanField(
        required=False,
        widget=CheckboxInput(attrs={"value": "False"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "dni",
            "is_active",
            "password",
        )