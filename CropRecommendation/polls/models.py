from django.db import models


class Crop(models.Model):
    N = models.FloatField()
    P = models.FloatField()
    k = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    notes = models.TextField()
    prediction_result = models.CharField(max_length=255, null=True)
    # prediction_result = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.notes

