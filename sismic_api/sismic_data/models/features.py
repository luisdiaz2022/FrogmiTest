"""Features Model."""

# Django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Feature(models.Model):

    external_id = models.CharField(max_length=255, blank=True)

    magnitude = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(-1.0), MaxValueValidator(10.0)]
        )
    
    mag_type = models.CharField(max_length=10)

    place = models.CharField(max_length=255)

    time = models.DateTimeField()

    url = models.CharField(max_length=255, null=False)

    tsunami = models.BooleanField(default=False)

    title = models.CharField(max_length=255, null=False)

    longitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        null=False,
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
        )
    
    latitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        null=False,
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
        )

    def __str__(self):
        return self.title