from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import date

# Create your models here.

class Feedback(models.Model):
"""Model for saving visitors' feedbacks and interacting with corresponding
database records.
"""
    user_name = models.CharField(max_length=60)
    text = models.TextField(max_length=1000)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return f"{self.text[:30]}... - {self.user_name}, {self.rating}"
