from django.db import models
from accounts.models import CustomUser
from employees.models import Employee



class ReportLog(models.Model):
    title = models.CharField(max_length=100, default=" ")
    REPORT_TYPES = (
        ('ATTENDANCE', 'Attendance'),
        ('LEAVE', 'Leave'),
        ('PAYROLL', 'Payroll'),
        ('PERFORMANCE', 'Performance'),
    )
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_by = models.ForeignKey(to=Employee, on_delete=models.SET_NULL, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default="This is test body...")
    file_path = models.FileField(upload_to='reports/')

    def __str__(self):
        return self.generated_at