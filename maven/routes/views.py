import requests
from rest_framework import viewsets
from django.http import JsonResponse
from .models import SafetyPoint
from .serializers import SafetyPointSerializer
from .models import RedZone, EmergencyContact
from .serializers import RedZoneSerializer, EmergencyContactSerializer

import requests
from rest_framework import viewsets
from django.http import JsonResponse

def get_osm_data(latitude, longitude, radius=1000):
    # Overpass API query to find police stations
    query = f"""
    [out:json];
    node
      [amenity=police]
      (around:{radius},{latitude},{longitude});
    out body;
    """
    response = requests.get(
        "https://overpass-api.de/api/interpreter",
        params={'data': query}
    )
    return response.json()

class SafetyPointViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        if not all([latitude, longitude]):
            return JsonResponse({"error": "Missing parameters"}, status=400)

        osm_data = get_osm_data(latitude, longitude)
        results = [
            {
                "name": element['tags'].get('name', 'Unnamed Police Station'),
                "vicinity": f"Lat: {element['lat']}, Lon: {element['lon']}",
                "place_id": element['id']
            }
            for element in osm_data['elements']
        ]
        return JsonResponse(results, safe=False)


class RedZoneViewSet(viewsets.ModelViewSet):
    queryset = RedZone.objects.all()
    serializer_class = RedZoneSerializer

class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
