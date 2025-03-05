from django.db import models

class Compra(models.Model):
    METODOS_PAGAMENTO = [
        ("cheque", "Cheque"),
        ("dinheiro", "Dinheiro"),
        ("credito", "Crédito"),
    ]

    fornecedor = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(  # AGORA ESTÁ PRESENTE NA DEFINIÇÃO FINAL
        max_length=10, choices=METODOS_PAGAMENTO, default="dinheiro"
    )
    status = models.CharField(
        max_length=10,
        choices=[("pendente", "Pendente"), ("pago", "Pago")],
        default="pendente"
    )

    def __str__(self):
        return f"{self.fornecedor} - R$ {self.valor} ({self.metodo_pagamento}, {self.status})"
