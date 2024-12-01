from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, dni, password, **extra_fields):
        if not username:
            raise ValueError("El nombre de usuario es requerido")
        if not dni:
            raise ValueError("La cédula de identidad es requerida")
        user = self.model(username=username, dni=dni, **extra_fields)
        user.set_password(password)
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
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["dni"]
