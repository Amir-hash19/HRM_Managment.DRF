from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.postgres.search import TrigramSimilarity
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import models
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
    username = models.CharField(max_length=100, unique=True, validators=[validate_username_with_special_characters])
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


#Person.people.all()
# class Person(models.Model):
#     people = models.Manager()
        


User = get_user_model()


def search_users(query):
    return User.objects.annotate(
        similarity=TrigramSimilarity('username', query)
    ).filter(similarity__gt=.03).order_by("-similarity")


