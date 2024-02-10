from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
LEVEL = [
    (100, 100),
    (200, 200),
    (300, 300),
    (400, 400),
    (500, 500)
]

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    def __str__(self):
        return self.email
    
class SocietyModel(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-name"]
        
    def __str__(self):
        return self.name
    
    
class UserRegistrar(models.Model):
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField()
    level = models.PositiveIntegerField(choices=LEVEL)
    IEEE_number = models.IntegerField(null=True, blank=True)
    societies = models.ManyToManyField(SocietyModel, related_name="societies_joined", blank=True)
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-email"]
    
    def __str__(self):
        return self.email
    

