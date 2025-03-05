from rest_framework import generics
from .models import Despesa
from .serializers import DespesaSerializer

class DespesaListCreateView(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
