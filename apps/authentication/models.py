from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from rest_framework_jwt.settings import api_settings

# JWT stuff
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# create your models here

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, first_name=None, last_name=None):
        if username is None:
            raise TypeError("User must have a username.")
        if email is None:
            raise TypeError("User must have an email.")

        # here we are creating the user object
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=False
        )

        user.set_password(password)
        user.save()

        from apps.api.models import Collection
        user.collection = Collection.objects.create(owner=user)

        return user

    def create_superuser(self, username, email, password=None, first_name=None, last_name=None):
        if password is None:
            raise TypeError("Superusers must have a password.")
        if username is None:
            raise TypeError("User must have a username.")
        if email is None:
            raise TypeError("User must have an email.")

        user = self.create_user(username, email, password, first_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        return token





