from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from users.manager import CustomUserManager
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True,null=True)

    USERNAME_FIELD = 'email' # Use Email instead of username
    REQUIRED_FIELDS = []

    objects = CustomUserManager()     
    def __str__(self):
        
        return self.email
    