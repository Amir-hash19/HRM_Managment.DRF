from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.db import models
from employees.models import Department
import re



class CustomUserManager(BaseUserManager):
    def create_user(self, phone, username=None, password=None, **extra_fields):
        if not phone:
            raise ValueError("phone number is required")
        if not username:
            raise ValueError("Username is required")
        user = self.model(phone=phone, username=username ,**extra_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password() 

        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, phone=None ,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone=phone, username=username, password=password, **extra_fields)
    







def validate_username_with_special_characters(value):
    if re.match(r'^[a-zA-Z0-9]*$', value):
        raise ValidationError("Username must contain at least one special charactes")
    


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, validators=validate_username_with_special_characters)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, region='IR')
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)

    slug = models.SlugField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


        


class AdminActivityLog(models.Model):
    admin_user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    detail = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return f"{self.admin_user} - {self.action} - {self.created_at}"
    




class Notifications(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    department = models.ForeignKey(to=Department, on_delete=models.SET_NULL, null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('sent', 'Sent')], default='pending')
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title