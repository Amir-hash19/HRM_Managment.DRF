from django.db import models
from accounts.models import CustomUser






class LeaveRequest(models.Model):
    LEAVE_TYPES = (
        ('ANNUAL', 'Annual Leave'),
        ('SICK', 'Sick Leave'),
        ('UNPAID', 'Unpaid Leave'),
    )
    STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled')
    )

    employee = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(blank=True, max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    reviewed_by = models.ForeignKey(to=CustomUser, null=True, blank=True, related_name='reviewed_leaves', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.reason
