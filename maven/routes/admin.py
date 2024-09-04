from django.contrib import admin
from .models import RedZone, SafetyPoint, EmergencyContact

# Register your models here.
admin.site.register(RedZone)
admin.site.register(SafetyPoint)
admin.site.register(EmergencyContact)