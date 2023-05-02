from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The email is not valid')
        email = self.normalize_email(email) # normalize_email is a built-in method that comes with BaseUserManager and it converts the email to lowercase
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        # extra_fields.setdefault('is_organizer', True)
        extra_fields.setdefault('super_user', True) # this is a boolean field that is set to True by default for superusers
        return self.create_user(username, email, password, **extra_fields)
    

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_organizer', False)
        extra_fields.setdefault('is_guest', False)
        extra_fields.setdefault('super_user', False)
        return self.create_user(username, email, password, **extra_fields)
    




class User(AbstractUser, PermissionsMixin): # permissionsMixin is a built-in model that comes with django and it gives us the ability to give permissions to users and groups and it also gives us the ability to check if a user has a specific permission
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_organizer = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    super_user = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']


    def __str__(self):
        return self.username