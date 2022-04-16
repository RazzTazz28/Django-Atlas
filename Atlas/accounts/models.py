
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime

from django.core.validators import MinLengthValidator

from .CHOICES import *
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
country_choice = COUNTRY_CHOICE


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)

        user.set_password(password)

        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=50, validators=[MinLengthValidator(8)], unique=True)

    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(3)], blank=False)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(3)], blank=False)

    #date_of_birth = models.DateField(blank=True)
    # month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], blank=False)
    # year = models.IntegerField(validators=[MinValueValidator(1942), MaxValueValidator(2017)], blank=False)

    # gender model
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=False)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICE, blank=False)

    datetime = models.DateTimeField(default=datetime.now())

    objects = CustomAccountManager()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    def __str__(self):
        return str(self.username)

