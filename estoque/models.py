from django.db import models

class Estoque(models.Model):
    UNIDADES_MEDIDA = [
        ("litros", "Litros"),
        ("sacas", "Sacas"),
        ("pacotes", "Pacotes"),
        ("unidades", "Unidades"),
        ("quilos", "Quilos"),
        ("garrafas", "Garrafas"),
    ]

    nome = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    unidade = models.CharField(max_length=10, choices=UNIDADES_MEDIDA, default="unidades")

    def __str__(self):
        return f"{self.nome} - {self.quantidade} {self.unidade}"
