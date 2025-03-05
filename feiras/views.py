from rest_framework import viewsets
from .models import Feira
from .serializers import FeiraSerializer

class FeiraViewSet(viewsets.ModelViewSet):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer
