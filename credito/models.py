from django.db import models

class CreditoCliente(models.Model):
    OPCOES_PRAZO = [
        ("semanal", "Semanal"),
        ("15dias", "15 dias"),
        ("45dias", "45 dias"),
    ]

    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    prazo = models.CharField(max_length=10, choices=OPCOES_PRAZO)
    status = models.CharField(max_length=20, default="por pagar")

    def __str__(self):
        return f"{self.nome} - R$ {self.valor} ({self.status})"
