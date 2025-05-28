from django.db import models
from accounts.models import CustomUser






class Payroll(models.Model):
    employee = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    month = models.DateField()  # usually the first day of the month
    base_salary = models.PositiveBigIntegerField()
    bonuses = models.PositiveIntegerField()
    deductions = models.PositiveBigIntegerField()
    finall_salary = models.PositiveBigIntegerField()
    generated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.base_salary