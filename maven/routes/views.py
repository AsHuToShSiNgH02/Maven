import requests
from rest_framework import viewsets
from django.http import JsonResponse
from .models import SafetyPoint
from .serializers import SafetyPointSerializer
from .models import RedZone, EmergencyContact
from .serializers import RedZoneSerializer, EmergencyContactSerializer

def get_nearby_places(latitude, longitude, place_type, radius=5000):
    api_key = 'AIzaSyDwFD35jG2lfNNRoxy6YfcL9C7d2CDjl7E'
    url = (
        f'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        f'?location={latitude},{longitude}'
        f'&radius={radius}&type={place_type}&key={api_key}'
    )
    response = requests.get(url)
    return response.json()

class SafetyPointViewSet(viewsets.ModelViewSet):
    queryset = SafetyPoint.objects.all()
    serializer_class = SafetyPointSerializer

    def list(self, request, *args, **kwargs):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        place_type = request.GET.get('type')

        if not all([latitude, longitude, place_type]):
            return JsonResponse({"error": "Missing parameters"}, status=400)

        places = get_nearby_places(latitude, longitude, place_type)
        return JsonResponse(places['results'], safe=False)
    
class RedZoneViewSet(viewsets.ModelViewSet):
    queryset = RedZone.objects.all()
    serializer_class = RedZoneSerializer

class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
