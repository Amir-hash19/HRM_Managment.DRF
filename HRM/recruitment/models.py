from django.db import models
from accounts.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField



class JobCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name



class JobPosition(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(to=JobCategory, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    job_description = models.TextField()
    requirements = models.TextField()
    bonus_Skills = models.TextField(null=True, blank=True)
    about_us = models.TextField(null=True, blank=True)
    required_Skills = models.TextField()


    Military_Service = (
        ("finished", "FINISHED"),
        ("no_matter", "NO_MATTER"),
        ("exemption_card", "EXEMPTIONـCARD")
        
    )
    military_service_status = models.CharField(max_length=100)
    minimum_education_requirement = models.CharField(max_length=255)


    EMPLOYMENT_TYPE = (
    ("full_time", "Full-time"),
    ("part_time", "Part-time"),
    ("contract", "Contract"),
    ("internship", "Internship"),
    ("remote", "Remote"),
    ("freelance", "Freelance"),
    )

    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    STATUS_JOB = (
        ("1", "REVIEWING RESUMES"),
        ("2", "RECEIVING APPLICATIONS"),
        ("3", "CLOSED")
    )
    position_status = models.CharField(max_length=50, choices=STATUS_JOB, default="2")
    is_immediate = models.BooleanField(default=False)

    GENDER_TYPE = (
        ("male", "MALE"),
        ("female", "FEMALE"),
        ("no_diffrence", "NO_DIFFRENCE")
    )
    gender_type = models.CharField(max_length=20, choices=GENDER_TYPE)
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
