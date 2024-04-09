from django.db import models

class Feature(models.Model):
    external_id = models.CharField(max_length=255)
    magnitude = models.DecimalField(max_digits=5, decimal_places=2)
    place = models.CharField(max_length=255)
    time = models.DateTimeField()
    tsunami = models.BooleanField(default=False)
    mag_type = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)

    def __str__(self):
        return self.title