from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# verify PermissionMixin for permissions

class User(AbstractBaseUser):

    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)


class CustomOwnerManager(BaseUserManager):
    def create_owner(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        # Normalizamos el email para que esté en minúsculas
        email = self.normalize_email(email)

        # Creamos el usuario con los campos adicionales
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Owner(AbstractBaseUser, PermissionsMixin):

        id = models.AutoField(primary_key=True)
        email = models.EmailField(unique=True)
        password = models.CharField(max_length=100)
        username = models.CharField(max_length=20, unique=True)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        date_joined = models.DateTimeField(auto_now_add=True)
        last_login = models.DateTimeField(null=True, blank=True)

        USERNAME_FIELDS = 'emails'
        REQUIRED_FIELDS =   ['first_name', 'last_name', 'password', 'username']

        objects = CustomOwnerManager()