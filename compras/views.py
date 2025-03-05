from rest_framework import viewsets
from .models import Compra
from .serializers import CompraSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by("-id")  # Ordena da mais recente para a mais antiga
    serializer_class = CompraSerializer
