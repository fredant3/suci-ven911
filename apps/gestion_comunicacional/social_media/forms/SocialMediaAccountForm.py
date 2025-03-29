from django.forms import ModelForm

from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity


class SocialMediaAccountForm(ModelForm):
    def __init__(self, *arg, **kwarg) -> None:
        super().__init__(*arg, **kwarg)
        self.fields["username_sm"].widget.attrs.update(
            {"placeholder": "Ingrese el usuario de la red social"}
        )
        self.fields["url"].widget.attrs.update(
            {"placeholder": "Ingrese la url de la red social"}
        )
        self.fields["followers"].widget.attrs.update(
            {"placeholder": "Ingrese la cantidad de seguidores de la red social"}
        )
        self.fields["responsible"].widget.attrs.update(
            {"placeholder": "Ingrese el usuario responsable de la red social"}
        )
        self.fields["publications"].widget.attrs.update(
            {"placeholder": "Ingrese la cantidad de publicaciones de la red social"}
        )
        for form in self.visible_fields():
            form.field.widget.attrs.update(
                {"class": "form-control", "autocomplete": "off"}
            )

    class Meta:
        model = SocialMediaAccountEntity
        fields = (
            "platform",
            "username_sm",
            "url",
            "followers",
            "responsible",
            "publications",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "delete_at",
            "delete_by",
        ]
        widgets = {}
