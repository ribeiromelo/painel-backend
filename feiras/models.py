from django.db import models

class Feira(models.Model):
    data = models.DateField()
    relatorio = models.TextField(blank=True, null=True)  # Relatório opcional
    valor_faturado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_fiado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Feira em {self.data} - Faturamento: R$ {self.valor_faturado}"
