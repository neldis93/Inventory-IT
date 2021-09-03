from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Managers
from .managers import UserManager

# register
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Username', max_length=50, unique=True)
    email= models.EmailField('Email', unique=True)
    first_name = models.CharField('First name', max_length=50)
    last_name= models.CharField('Last name', max_length=50)
    phone= models.CharField('Phone',max_length=20,blank=True, null= True)
    is_staff= models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= ['email']

    objects= UserManager()

    def __str__(self):
        return self.username
