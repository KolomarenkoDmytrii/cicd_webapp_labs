from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Feedback(models.Model):
    user_name = models.CharField(max_length=60)
    text = models.TextField(max_length=1000)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
