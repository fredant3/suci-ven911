from django import forms


class FormBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        # TODO: Validar si el input es un select agrgar esta clase (form-select)
        # TODO: si es un input agregar la clase (form-control)
        # TODO: investigar como poner en el label la clase (text-end)

    def create_date_field(field_name):
        return forms.DateField(
            widget=forms.TextInput(attrs={"type": "date"}),
            input_formats=["%d/%m/%Y"],
            error_messages={"invalid": "Ingrese la fecha en el formato DD/MM/YYYY."},
            label=field_name.capitalize(),
        )
