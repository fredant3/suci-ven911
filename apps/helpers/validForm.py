import re
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


# Valida que el valor sea un número entero positivo.
def validate_cantidad(value, msg="La cantidad debe ser un número entero positivo."):
    if not re.match(r"^\d+$", str(value)):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
# TODO: ver que patron de sserial tiene que ser
def validate_serial(
    value, msg="El serial solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
# TODO: ver que patron de sserial tiene que ser
def validate_codigo_bn(
    value, msg="El código BN solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
# TODO: ver que patron de sserial tiene que ser
def validate_n_orden(
    value, msg="El número de orden solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras y espacios.
def validate_nombre(value, msg="El nombre solo puede contener letras y espacios."):
    if not re.match(r"^[a-zA-Z\s]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números y guiones.
# TODO: ver que patron de sserial tiene que ser
def validate_placa(
    value, msg="La placa solo puede contener letras, números y guiones."
):
    if not re.match(r"^[a-zA-Z0-9\-]+$", value):
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
def validate_telefono(
    value,
    msg="El teléfono solo puede contener números y guiones. Debe tener la estructura 0412-3456789 o 04123456789",
):

    if not re.match(r"^(\+?58)?(0?4\d{9})$", value):
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
def validate_general_text_solicitud(
    value,
    msg="El motivo de la solicitud solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor contenga solo letras, números, espacios y los caracteres .,-!?().
def validate_general_text_solicita(
    value,
    msg="El ente que solicita solo puede contener letras, números, espacios y los caracteres .,-!?().",
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea una URL válida.
def validate_url(value, message):
    validator = URLValidator()
    try:
        validator(value)
    except ValidationError:
        raise ValidationError(message)


def validate_general_text(
    value, msg="Solo se permiten letras, números, espacios y los caracteres .,-!?()."
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-!?()]+$", value):
        raise ValidationError(msg)


def validate_basic_text(
    value, msg="Solo se permiten letras, números, espacios y los caracteres .,-."
):
    if not re.match(r"^[a-zA-Z0-9\s\.,\-]+$", value):
        raise ValidationError(msg)


def validate_decimal_number(
    value, msg="Debe ser un número positivo con hasta dos decimales."
):
    if not re.match(r"^\d+(\.\d{1,2})?$", str(value)):
        raise ValidationError(msg)
