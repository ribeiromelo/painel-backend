from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """ Modelo de Usuário Personalizado """
    pass  # Podemos adicionar mais campos personalizados depois

    def __str__(self):
        return self.username

