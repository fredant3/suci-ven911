from users.auth.models import User


class UserFaker:
    def admin_user():
        admin = User.objects.filter(dni="100").first()
        if admin is None:
            admin = User.objects.create(
                username="100",
                dni="100",
                password="pbkdf2_sha256$720000$Kz9kinsPg3DmSui1Piw5vy$P9/hiiwNCkYmFuXdDLrP8ZVXctTk7eU0odL2FIMmeEU=",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            print(
                f"Usuario {admin.username} con cédula de identidad {admin.username} creado como superusuario, su contraseña: admin"
            )

        return admin

    def guest_user():
        guest = User.objects.filter(dni="200").first()
        if guest is None:
            guest = User.objects.create(
                username="200",
                dni="200",
                password="pbkdf2_sha256$720000$4ojJVNjkvfY3KcZsqfYIgu$ZWb6ndDEB96vo0mTbmIEIXJaxT7wbCVdWisnm0irPFA=",
                is_staff=True,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {guest.username} con cédula de identidad {guest.username} creado como usuario, su contraseña: guest"
            )

        return guest

    def other_user():
        other = User.objects.filter(dni="300").first()
        if other is None:
            other = User.objects.create(
                username="300",
                dni="300",
                password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",
                is_staff=False,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {other.username} con cédula de identidad {other.username} creado como usuario, su contraseña: other"
            )

        return other
