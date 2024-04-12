"""Comments Model."""

# Utilities
from django.utils import timezone

# Django
from django.db import models

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment {self.id} for Feature {self.feature.id}"