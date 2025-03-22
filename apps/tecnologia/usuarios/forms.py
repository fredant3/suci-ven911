from users.auth.models import User
from helpers.FormBase import FormBase


class UserForm(FormBase):
    class Meta:
        model = User
        fields = (
            "username",
            "dni",
            "is_active",
            "password",
        )
