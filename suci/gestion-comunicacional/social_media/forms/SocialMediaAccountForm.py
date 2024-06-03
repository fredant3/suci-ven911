from django.forms import ModelForm
from entities.SocialMediaAccountEntity import SocialMediaAccountEntity


class SocialMediaAccountForm(ModelForm):
    class Meta:
        model = SocialMediaAccountEntity
        fields = (
            "platform",
            "username",
            "url",
            "followers",
            "responsible",
            "publications",
        )
