from rest_framework import serializers
from .models import CreditoCliente

class CreditoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditoCliente
        fields = '__all__'

    def validate(self, data):
        # Garantir que o valor seja positivo
        if data["valor"] <= 0:
            raise serializers.ValidationError({"valor": "O valor deve ser maior que zero."})

        # Garantir que o prazo seja uma das opções permitidas
        opcoes_prazo = ["semanal", "15dias", "45dias"]
        if data["prazo"] not in opcoes_prazo:
            raise serializers.ValidationError({"prazo": "Opção inválida. Escolha: Semanal, 15dias ou 45dias."})

        return data
