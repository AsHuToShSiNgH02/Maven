
from rest_framework import serializers
from .models import SafetyPoint, RedZone, EmergencyContact

class SafetyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyPoint
        fields = '__all__'

class RedZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedZone
        fields = '__all__'

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'
