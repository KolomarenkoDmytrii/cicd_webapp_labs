from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name)


class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    min_terms = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(
        default=0,
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    slug = models.SlugField()

    class Meta:
        ordering = ["category__name", "name"]

    def __str__(self):
        return (
            f"{self.category} | {self.name}: min {self.min_terms} днів, {self.price}₴"
        )
