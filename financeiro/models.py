from django.db import models

class Despesa(models.Model):
    CATEGORIAS = [
        ("Trabalhadores", "Trabalhadores"),
        ("Combustível", "Combustível"),
        ("Descarregamento", "Descarregamento"),
        ("Peças", "Peças"),
        ("Serviços", "Serviços"),
        ("Tecnologia", "Tecnologia"),
        ("Construção", "Construção"),
    ]

    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="Trabalhadores")
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} ({self.categoria})"
