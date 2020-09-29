from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    username    = None
    email       = models.EmailField(verbose_name='Email Address', unique=True)
    name        = models.CharField(max_length=100)
    slot        = models.IntegerField(default=0)
    start_time  = models.DateTimeField(null=True, blank=True)
    points      = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email