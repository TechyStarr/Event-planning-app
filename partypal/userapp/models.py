from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The username is not valid')
        email = self.normalize_email(email) # normalize_email is a built-in method that comes with BaseUserManager and it converts the email to lowercase
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_organizer', True)
        extra_fields.setdefault('is_guest', True)
        extra_fields.setdefault('super_user', True)
        return self.create_user(username, password, **extra_fields)
    




class User(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username