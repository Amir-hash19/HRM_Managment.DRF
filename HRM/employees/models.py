from django.db import models
from accounts.models import CustomUser
from django.core.exceptions import ValidationError


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    




def validate_iranian_national_id(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("National ID must be exactly 10 digits.")
    
    check = int(value[-1])
    s = sum(int(value[i]) * (10 - i) for i in range(9))
    r = s % 11

    if (r < 2 and check != r) or (r >= 2 and check != (11 - r)):
        raise ValidationError("Invalid national ID.")
    



class Employee(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, related_name="employee_profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100, unique=True)
    national_id = models.CharField(max_length=10, unique=True, validators=[validate_iranian_national_id])
    birth_date = models.DateField(null=True, blank=True)

    GENDER_TYPE=(
        ("1", "MALE"),
        ("2", "FEMALE")
    )

    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    job_title = models.CharField(max_length=200)
    department = models.ForeignKey(to=Department, on_delete=models.SET_NULL, null=True, related_name="department_employee")
    manager = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    hire_date = models.DateField()

    CONTRACT_TYPE = (
        ("full_time", "FULL_TIME"),
        ("part_time", "PART_TIME"),
        ('Contract', 'CONTRACT'),
        ("intern", "INTERN")
    )

    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE)
    salary = models.PositiveBigIntegerField()
    address = models.TextField()
    emergency_contact = models.CharField(max_length=100, blank=True)

    POSITION_TYPE = (
        ("1", "JUNIUR"),
        ("2", "MID_LEVEL"),
        ("3", "SINIUR"),
        ("4", "MANAGER"),
        ("5", "INTERNSHIP")
    )
    position = models.CharField(max_length=50, choices=POSITION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f"{self.first_name}-{self.last_name}"




class EmployeeLogs(models.Model):
    employee_id = models.CharField(max_length=100, unique=True)
    employee_user = models.ForeignKey(to=Employee, on_delete=models.SET_NULL, null=True)
    detail = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.employee_id}--{self.created_at}"
