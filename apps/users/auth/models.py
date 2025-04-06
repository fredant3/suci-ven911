from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from helpers.models import BOOLEAN_CHOICES


class UserManager(BaseUserManager):
    def create_user(self, username, dni, password, **extra_fields):
        if not username:
            raise ValueError("El nombre de usuario es requerido")
        if not dni:
            raise ValueError("La cédula de identidad es requerida")
        user = self.model(username=username, dni=dni, **extra_fields)
        user.set_password("SUCI-Ven911")
        user.save()
        return user

    def create_superuser(self, username, dni, password):
        user = self.create_user(username, dni, password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    dni = models.CharField(max_length=12, unique=True)
    is_staff = models.BooleanField(choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1])
    is_active = models.BooleanField(choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1])
    is_superuser = models.BooleanField(
        choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1]
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["dni"]
