from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password,first_name,last_name):
        
        if not email:
            raise ValueError(_("The Email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, 
                          first_name=first_name,
                          last_name=last_name)
        
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password,first_name,last_name):
        
        user = self.create_user(email=email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email