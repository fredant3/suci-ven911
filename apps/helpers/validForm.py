import re
from django.core.exceptions import ValidationError


# Valida que el valor sea un número entero positivo.
def validate_cantidad(value, msg="La cantidad debe ser un número entero positivo."):
    if not re.match(r"^\d+$", str(value)):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-.
def validate_descripcion(
    value,
    msg="La descripción solo puede contener letras, números, espacios y los caracteres .,-.",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_observaciones(
    value,
    msg="Las observaciones solo pueden contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_problema(
    value,
    msg="El problema solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-.
def validate_ubicacion(
    value,
    msg="La ubicación solo puede contener letras, números, espacios y los caracteres .,-.",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
def validate_serial(
    value, msg="El serial solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
def validate_codigo_bn(
    value, msg="El código BN solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
def validate_n_orden(
    value, msg="El número de orden solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea un número positivo, permitiendo hasta dos decimales.
def validate_valor_bs(
    value, msg="El valor en BS debe ser un número positivo con hasta dos decimales."
):
    if not re.match(r"^\d+(\.\d{1,2})?$", str(value)):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras y espacios.
def validate_nombre(value, msg="El nombre solo puede contener letras y espacios."):
    if not re.match(r"^[a-zA-Z\s]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-.
def validate_marca(
    value,
    msg="La marca solo puede contener letras, números, espacios y los caracteres .,-.",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-.
def validate_modelo(
    value,
    msg="El modelo solo puede contener letras, números, espacios y los caracteres .,-.",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
def validate_placa(
    value, msg="La placa solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea un número positivo, permitiendo hasta dos decimales.
def validate_cantidad_combustible(
    value,
    msg="La cantidad de combustible debe ser un número positivo con hasta dos decimales.",
):
    if not re.match(r"^\d+(\.\d{1,2})?$", str(value)):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-.
def validate_condicion(
    value,
    msg="La condición solo puede contener letras, números, espacios y los caracteres .,-.",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-]+$", value):
        raise ValidationError(msg)


def validate_sede(
    value, msg="El nombre de la sede solo puede contener letras, números y espacios."
):
    if not re.match(r"^[a-zA-Z0-9\s]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras y espacios.
def validate_nombres_apellidos(
    value, msg="Este campo solo puede contener letras y espacios."
):
    if not re.match(r"^[a-zA-Z\s]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea un número de cédula válido (solo números y guiones).
def validate_cedula(value, msg="La cédula solo puede contener números y guiones."):
    if not re.match(r"^[0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea un número de teléfono válido (solo números y guiones).
def validate_telefono(value, msg="El teléfono solo puede contener números y guiones."):
    if not re.match(r"^[0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea una dirección válida (letras, números, espacios y caracteres comunes).
def validate_direccion(
    value,
    msg="La dirección solo puede contener letras, números, espacios y los caracteres .,-.",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea un correo electrónico válido.
def validate_email(value, msg="Ingrese un correo electrónico válido."):
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_ente(
    value,
    msg="El ente solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_motivo(
    value,
    msg="El motivo solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_zona(
    value,
    msg="La zona solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_camara(
    value,
    msg="El campo cámara solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_motivo_solicitud(
    value,
    msg="El motivo de la solicitud solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_ente_solicita(
    value,
    msg="El ente que solicita solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)
