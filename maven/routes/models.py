from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SafetyPoint(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    feature_type = models.CharField(max_length=50)  # e.g., "Police Station", "Red Light", "CCTV"

    def __str__(self):
        return f"{self.name} - {self.feature_type}"
    
class RedZone(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()  # in meters
    description = models.TextField()

    def __str__(self):
        return self.name

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.phone_number})"


    