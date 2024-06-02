from django.forms import ModelForm
from .models import SocialMediaAccount


class CreateSocialMediaAccount(ModelForm):
    class Meta:
        model = SocialMediaAccount
        fields = (
            "platform",
            "username",
            "url",
        )


class UpdateSocialMediaAccount(ModelForm):
    class Meta:
        model = SocialMediaAccount
        fields = (
            "platform",
            "username",
            "url",
        )
