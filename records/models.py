from django.db import models

# Create your models here.
from django.db import models

class TemperatureRecord(models.Model):
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperature}°C at {self.timestamp}"