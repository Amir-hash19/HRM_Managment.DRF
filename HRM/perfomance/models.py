from django.db import models
from accounts.models import CustomUser



class PerformanceReview(models.Model):
    employee = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(to=CustomUser, related_name='performance_reviews_given', on_delete=models.SET_NULL, null=True)
    period_start = models.DateField()
    period_end = models.DateField()
    score = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug
