import re
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


# Valida que el valor sea un número de cédula válido (solo números y guiones).
def validate_cedula(value, msg="La cédula solo puede contener números y guiones."):
    if not re.match(r"^[0-9\-]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea un correo electrónico válido.
def validate_email(value, msg="Ingrese un correo electrónico válido."):
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
        raise ValidationError(msg)


# Valida que el valor sea una URL válida.
def validate_url(value, message):
    validator = URLValidator()
    try:
        validator(value)
    except ValidationError:
        raise ValidationError(message)


def validate_decimal_number(
    value, msg="Debe ser un número positivo con hasta dos decimales."
):
    if not re.match(r"^\d+(\.\d{1,2})?$", str(value)):
        raise ValidationError(msg)


@deconstructible
class PositiveIntegerValidator:
    messages = {
        "invalid": "Introduzca un número entero positivo",
        "not_integer": "Asegúrese de que este valor sea un entero (%(type)s recibido).",
        "not_positive": "Asegúrese de que este valor sea mayor que 0 (%(valor)s recibidos)",
    }

    def __init__(self, message=None):
        if message is not None:
            self.messages["invalid"] = message

    def __call__(self, value):
        if not isinstance(value, int):
            raise ValidationError(
                self.messages["not_integer"],
                code="not_integer",
                params={"type": type(value).__name__, "value": value},
            )

        if value <= 0:
            raise ValidationError(
                self.messages["not_positive"],
                code="not_positive",
                params={"value": value},
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.messages["invalid"] == other.messages["invalid"]
        )


@deconstructible
class MinIntegerValidator:
    messages = {
        "invalid": "Introduzca un número entero",
        "min_value": "Asegúrese de que este valor sea mayor o igual a %(limit_value)s (%(value)s recibido).",
    }

    def __init__(self, min_value=None, message=None):
        self.min_value = min_value if min_value is not None else 1
        if message is not None:
            self.messages["min_value"] = message

    def __call__(self, value):
        if not isinstance(value, int):
            raise ValidationError(
                self.messages["invalid"],
                code="invalid",
                params={"value": value},
            )

        if value < self.min_value:
            raise ValidationError(
                self.messages["min_value"],
                code="min_value",
                params={"value": value, "limit_value": self.min_value},
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and (self.min_value == other.min_value)
            and (self.messages["min_value"] == other.messages["min_value"])
        )


@deconstructible
class TextValidator:
    default_message = _(
        "Solo se permiten letras, números, espacios y los caracteres: "
        ".,;:¿?¡!()-'\"@/"
    )

    pattern = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\.,;:¿?¡!\(\)\-\'"@/]+$'

    def __init__(self, message=None, extra_chars=None):
        if message:
            self.message = message
        else:
            self.message = self.default_message

        if extra_chars:
            self.pattern = f"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\\s\\.,;:¿?¡!\\(\\)\\-'\"@/{re.escape(extra_chars)}]+$"

    def __call__(self, value):
        if not re.match(self.pattern, str(value)):
            raise ValidationError(self.message, code="invalid", params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.message == other.message
            and self.pattern == other.pattern
        )


@deconstructible
class UnicodeAlphaSpaceValidator:
    messages = {
        "invalid": "Solo se permiten letras y espacios.",
        "invalid_chars": "Caracteres no permitidos: %(invalid_chars)s",
        "invalid_type": "Tipo de dato inválido. Se esperaba una cadena, recibido: %(type)s",
    }

    default_regex = r"^[\p{L}\s]+$"

    def __init__(self, message=None, extra_chars=None):
        self.regex = self.default_regex

        if extra_chars:
            self.regex = f"^[\\p{{L}}\\s{re.escape(extra_chars)}]+$"

        if message:
            self.messages = self.messages.copy()
            self.messages["invalid"] = message

    def __call__(self, value):
        str_value = str(value)

        if not isinstance(value, (str, int, float)):
            raise ValidationError(
                self.messages["invalid_type"],
                code="invalid_type",
                params={"type": type(value).__name__},
            )

        if not re.match(self.regex, str_value, flags=re.UNICODE):
            invalid_chars = set()
            for char in str_value:
                if not re.match(r"[\p{L}\s]", char, flags=re.UNICODE):
                    invalid_chars.add(char)
                    if len(invalid_chars) >= 3:
                        break

            if invalid_chars:
                raise ValidationError(
                    self.messages["invalid_chars"],
                    code="invalid_chars",
                    params={"invalid_chars": "".join(sorted(invalid_chars))},
                )
            else:
                raise ValidationError(
                    self.messages["invalid"], code="invalid", params={"value": value}
                )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.messages == other.messages
            and self.regex == other.regex
        )


@deconstructible
class PhoneNumberValidator:
    """
    Valida números telefónicos con formatos internacionales comunes.
    Soporta:
    - Venezuela: 0412-1234567, 04121234567, +584121234567
    - Internacional: +1 (123) 456-7890, +34 912 34 56 78
    """

    messages = {
        "invalid": _("Formato de teléfono inválido."),
        "invalid_format": _("El formato debe ser: %(expected_format)s"),
        "invalid_chars": _("Caracteres no permitidos: %(invalid_chars)s"),
        "min_length": _("El número debe tener al menos %(min_length)d dígitos."),
    }

    # Expresiones regulares para formatos comunes
    FORMATS = {
        "ve": r"^(\+?58)?(0?4\d{2}[-\. ]?\d{7})$",  # Venezuela
        "intl": r"^\+(?:[0-9] ?){6,14}[0-9]$",  # Internacional E.164
        "simple": r"^[\d\s\-\.\(\)\+]+$",  # Validación básica
    }

    def __init__(self, country="ve", message=None, min_length=7):
        """
        Args:
            country (str): Código de país ('ve' para Venezuela, 'intl' para internacional)
            message (str): Mensaje personalizado para el error 'invalid'
            min_length (int): Longitud mínima requerida (sin contar símbolos)
        """
        self.country = country.lower()
        self.min_length = min_length

        if message:
            self.messages = self.messages.copy()
            self.messages["invalid"] = message

    def __call__(self, value):
        str_value = str(value).strip()

        # Validación básica de caracteres
        if not re.match(self.FORMATS["simple"], str_value):
            invalid_chars = set(re.findall(r"[^\d\s\-\.\(\)\+]", str_value))
            raise ValidationError(
                self.messages["invalid_chars"],
                code="invalid_chars",
                params={"invalid_chars": "".join(invalid_chars)},
            )

        # Extraer solo dígitos para validar longitud
        digits = re.sub(r"[^\d]", "", str_value)
        if len(digits) < self.min_length:
            raise ValidationError(
                self.messages["min_length"],
                code="min_length",
                params={"min_length": self.min_length},
            )

        # Validación específica por país
        if not re.match(self.FORMATS[self.country], str_value):
            expected_format = {
                "ve": "0412-1234567, 04121234567 o +584121234567",
                "intl": "+[código país][número] ej: +581234567890",
            }.get(self.country, "")

            raise ValidationError(
                self.messages["invalid_format"],
                code="invalid_format",
                params={"expected_format": expected_format},
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and (self.country == other.country)
            and (self.min_length == other.min_length)
            and (self.messages == other.messages)
        )
