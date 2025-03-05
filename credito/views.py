from rest_framework import viewsets
from .models import CreditoCliente
from .serializers import CreditoClienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class CreditoClienteViewSet(viewsets.ModelViewSet):
    queryset = CreditoCliente.objects.all()
    serializer_class = CreditoClienteSerializer

    # Permite visualizar tanto "por pagar" quanto "pago"
    def get_queryset(self):
        status_filtro = self.request.query_params.get("status", None)
        if status_filtro:
            return CreditoCliente.objects.filter(status=status_filtro)
        return CreditoCliente.objects.all()

    # Adiciona a opção de atualizar o status pelo PATCH
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data.get("status", instance.status)
        instance.save()
        return Response({"status": "Atualizado com sucesso!"}, status=status.HTTP_200_OK)

    # Adiciona uma ação para marcar como pago
    @action(detail=True, methods=['post'])
    def marcar_como_pago(self, request, pk=None):
        credito = self.get_object()
        credito.status = "pago"
        credito.save()
        return Response({"status": "Atualizado para pago!"})
