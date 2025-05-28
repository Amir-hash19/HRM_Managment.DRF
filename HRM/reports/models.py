from django.db import models
from accounts.models import CustomUser




class ReportLog(models.Model):
    REPORT_TYPES = (
        ('ATTENDANCE', 'Attendance'),
        ('LEAVE', 'Leave'),
        ('PAYROLL', 'Payroll'),
        ('PERFORMANCE', 'Performance'),
    )
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_by = models.ForeignKey(to=CustomUser, on_delete=models.SET_NULL, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.FileField(upload_to='reports/')