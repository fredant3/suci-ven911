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
        "not_positive": "Asegúrese de que este valor sea mayor que 0 (%(value)s recibidos)",
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

        if value < 0:
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
        self.regex = self.default_regex = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"

        if extra_chars:
            self.regex = f"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s{re.escape(extra_chars)}]+$"

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
                if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]$", char, flags=re.UNICODE):
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


@deconstructible
class CedulaVenezolanaValidator:
    """
    Valida cédulas de identidad venezolanas con formatos:
    - 12345678
    - V12345678
    - V-12345678
    - V-12.345.678
    También valida el dígito verificador cuando está completo (opcional)
    """

    messages = {
        "invalid": _("Formato de cédula inválido."),
        "invalid_format": _(
            "El formato debe ser: 12345678, V12345678, V-12345678 o V-12.345.678"
        ),
        "invalid_chars": _(
            "Solo se permiten números, guiones, puntos y la letra V opcional"
        ),
        "verification_failed": _("El dígito verificador no es válido"),
        "length_error": _("La cédula debe tener entre 6 y 8 dígitos"),
    }

    # Expresión regular para los formatos aceptados (V opcional)
    FORMAT_REGEX = r"^(V[-]?)?(\d{1,3}(?:\.?\d{3}){1,2}|\d{6,8})$"

    def __init__(self, validate_verifier=False, message=None):
        """
        Args:
            validate_verifier (bool): Si True, valida el dígito verificador (para cédulas completas)
            message (str): Mensaje personalizado para el error 'invalid'
        """
        self.validate_verifier = validate_verifier
        if message:
            self.messages = self.messages.copy()
            self.messages["invalid"] = message

    def __call__(self, value):
        str_value = str(value).strip().upper()

        # Validación básica de caracteres (V opcional)
        if not re.match(r"^(V[-\.\d]+|\d+)$", str_value):
            invalid_chars = set(re.findall(r"[^V\d\-\.]", str_value))
            raise ValidationError(
                self.messages["invalid_chars"],
                code="invalid_chars",
                params={"invalid_chars": "".join(invalid_chars)},
            )

        # Validación del formato
        if not re.match(self.FORMAT_REGEX, str_value):
            raise ValidationError(
                self.messages["invalid_format"],
                code="invalid_format",
                params={"value": value},
            )

        # Extraer solo los dígitos
        if str_value.startswith("V"):
            digits = re.sub(r"[^\d]", "", str_value[1:])  # Excluye la V inicial
        else:
            digits = re.sub(r"[^\d]", "", str_value)  # Toda la cadena son dígitos

        # Validar longitud
        if len(digits) < 6 or len(digits) > 8:
            raise ValidationError(
                self.messages["length_error"],
                code="length_error",
                params={"value": value},
            )

        # Validar dígito verificador (si está configurado)
        if self.validate_verifier and len(digits) == 8:
            if not self._validate_verification_digit(digits):
                raise ValidationError(
                    self.messages["verification_failed"],
                    code="verification_failed",
                    params={"value": value},
                )

    def _validate_verification_digit(self, digits):
        """
        Implementa el algoritmo de validación del dígito verificador
        para cédulas venezolanas (opcional)
        """
        # Algoritmo de validación del dígito verificador
        # (Implementación real dependerá del algoritmo oficial)
        base = digits[:-1]
        verifier = digits[-1]

        # Ejemplo simplificado (reemplazar con algoritmo real)
        total = sum(int(d) for d in base)
        calculated_verifier = total % 10

        return str(calculated_verifier) == verifier

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and (self.validate_verifier == other.validate_verifier)
            and (self.messages == other.messages)
        )


import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class CurrencyValidator:
    """
    Valida diferentes formatos de moneda, incluyendo:
    - Bolívares venezolanos: Bs. 1.234,56 / Bs 1.234,56 / 1.234,56 Bs.
    - Dólares y otras monedas internacionales: $1,234.56 / USD 1,234.56 / 1,234.56 USD
    - Formatos europeos: 1 234,56 € / 1.234,56 EUR
    - Formatos simplificados: 1234.56 / 1234,56
    """

    messages = {
        "invalid": _(
            "Formato de moneda inválido. Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"
        ),
        "invalid_format": _("El formato debe ser: %(expected_format)s"),
        "negative": _("El valor no puede ser negativo."),
        "max_decimal": _("No puede tener más de %(max)d decimales."),
    }

    # Expresiones regulares para diferentes formatos de moneda
    CURRENCY_PATTERNS = {
        "bs": r"^(Bs\.?)\s*(\d{1,3}(?:\.\d{3})*(?:,\d{1,2})?)$",  # Bolívares
        "usd": r"^(\$|USD\s*)(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)$",  # Dólares
        "eur": r"^(\d{1,3}(?:\.\d{3})*(?:,\d{1,2})?)\s*(€|EUR)?$",  # Euros
        "general": r"^(\d{1,3}(?:[.,\s]\d{3})*(?:[.,]\d{1,2})?)$",  # Formato general
    }

    def __init__(
        self, currency_type=None, allow_negative=False, max_decimal=2, message=None
    ):
        """
        Args:
            currency_type (str): Tipo de moneda específico ('bs', 'usd', 'eur' o None para cualquiera)
            allow_negative (bool): Si permite valores negativos
            max_decimal (int): Máximo número de decimales permitidos
            message (str): Mensaje personalizado para el error 'invalid'
        """
        self.currency_type = currency_type.lower() if currency_type else None
        self.allow_negative = allow_negative
        self.max_decimal = max_decimal

        if message:
            self.messages = self.messages.copy()
            self.messages["invalid"] = message

    def __call__(self, value):
        if isinstance(value, (int, float)):
            # Si es un número, validamos directamente
            self._validate_numeric(value)
            return

        str_value = str(value).strip()

        # Verificar si es negativo
        if not self.allow_negative and "-" in str_value:
            raise ValidationError(
                self.messages["negative"],
                code="negative",
            )

        # Limpiar múltiples espacios
        str_value = re.sub(r"\s+", " ", str_value)

        # Validar según el tipo de moneda específico o probar todos los formatos
        if self.currency_type:
            self._validate_specific_currency(str_value)
        else:
            self._validate_general_currency(str_value)

    def _validate_numeric(self, value):
        """Valida valores numéricos directamente"""
        if not self.allow_negative and value < 0:
            raise ValidationError(
                self.messages["negative"],
                code="negative",
            )

        # Verificar decimales para valores numéricos
        if isinstance(value, float):
            decimal_part = str(value).split(".")[1]
            if len(decimal_part) > self.max_decimal:
                raise ValidationError(
                    self.messages["max_decimal"],
                    code="max_decimal",
                    params={"max": self.max_decimal},
                )

    def _validate_specific_currency(self, value):
        """Valida un tipo de moneda específico"""
        pattern = self.CURRENCY_PATTERNS.get(self.currency_type)

        if not pattern or not re.match(pattern, value, flags=re.IGNORECASE):
            expected_formats = {
                "bs": "Bs. 1.234,56 o 1.234,56 Bs.",
                "usd": "$1,234.56 o USD 1,234.56",
                "eur": "1.234,56 € o 1 234,56 EUR",
            }

            raise ValidationError(
                self.messages["invalid_format"],
                code="invalid_format",
                params={
                    "expected_format": expected_formats.get(self.currency_type, "")
                },
            )

        # Validar decimales
        self._validate_decimal_part(value)

    def _validate_general_currency(self, value):
        """Valida cualquier formato de moneda reconocido"""
        matched = False

        for pattern in self.CURRENCY_PATTERNS.values():
            if re.match(pattern, value, flags=re.IGNORECASE):
                matched = True
                break

        if not matched:
            # Intentar con formato numérico simple
            if not re.match(r"^-?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{1,2})?$", value):
                raise ValidationError(
                    self.messages["invalid"],
                    code="invalid",
                )

        # Validar decimales
        self._validate_decimal_part(value)

    def _validate_decimal_part(self, value):
        """Valida la parte decimal del valor"""
        # Encontrar el separador decimal (puede ser . o ,)
        decimal_sep = "," if "," in value else "." if "." in value else None

        if decimal_sep:
            # Extraer parte decimal
            decimal_part = value.split(decimal_sep)[-1]
            decimal_part = re.sub(r"[^\d]", "", decimal_part)

            if len(decimal_part) > self.max_decimal:
                raise ValidationError(
                    self.messages["max_decimal"],
                    code="max_decimal",
                    params={"max": self.max_decimal},
                )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and (self.currency_type == other.currency_type)
            and (self.allow_negative == other.allow_negative)
            and (self.max_decimal == other.max_decimal)
            and (self.messages == other.messages)
        )
