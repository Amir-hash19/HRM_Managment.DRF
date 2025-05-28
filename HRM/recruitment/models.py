from django.db import models
from accounts.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField



class JobPosition(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    about_us = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title





class Applicant(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True, region='IR')
    applied_position = models.ForeignKey(to=JobPosition, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=[('NEW', 'New'), ('INTERVIEW', 'Interview'), ('HIRED', 'Hired'), ('REJECTED', 'Rejected')], default='NEW')
    applied_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.full_name
