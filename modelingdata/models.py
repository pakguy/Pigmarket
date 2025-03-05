from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
# models.py
class CustomUser(AbstractUser):
    # Remove default username and use email as the login identifier
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={'unique': 'A user with that username already exists.'},
        blank=False,  # Make username required
        null=False,
    )
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    
    
    # Use email for authentication (USERNAME_FIELD), but keep username as a separate field
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  # Fields prompted during createsuperuser

    def __str__(self):
        return self.email


# model for breeds
class  Breeds(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

# model for tags
class TagsColour(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

# model for sex
class Sex(models.Model):
    name = models.CharField(max_length=222)
    def __str__(self):
        return self.name

# Create your models here.
