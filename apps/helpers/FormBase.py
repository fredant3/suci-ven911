from django import forms


class FormBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        # TODO: Validar si el input es un select agrgar esta clase (form-select)
        # TODO: si es un input agregar la clase (form-control)
        # TODO: investigar como poner en el label la clase (text-end)
