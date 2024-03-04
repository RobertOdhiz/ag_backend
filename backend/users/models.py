from basemodel.models import BaseModel
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_farmer', True)

        if not email:
            raise ValueError(gettext_lazy("Please provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_farmer', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        user = self.create_user(email, first_name, last_name, password, **other_fields)
        return user


class NewUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    first_name = models.CharField(default="", max_length=250, blank=True)
    last_name = models.CharField(default="", max_length=250)
    is_staff = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

