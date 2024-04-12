from django.db import models
from django.utils import timezone

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment {self.id} for Feature {self.feature.id}"