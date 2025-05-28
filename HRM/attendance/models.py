from django.db import models
from accounts.models import CustomUser




class Attendance(models.Model):
    employee = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    is_absent = models.BooleanField(default=False)

    def __str__(self):
        return self.date