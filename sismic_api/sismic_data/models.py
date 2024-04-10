from django.db import models

class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=255, null=True)
    magnitude = models.DecimalField(max_digits=5, decimal_places=2)
    place = models.CharField(max_length=255)
    time = models.TimeField()
    url = models.CharField(max_length=255, null=False)
    tsunami = models.BooleanField(default=False)
    mag_type = models.CharField(max_length=10)
    title = models.CharField(max_length=255, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=False)

    def __str__(self):
        return self.title