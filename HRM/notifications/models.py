from django.db import models
from accounts.models import CustomUser




class Notification(models.Model):
    recipient = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    

    