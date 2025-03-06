import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "painel_cereais.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
password = "H2esolu##"
email = "contatoeriquemelo@gmail.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superusuário '{username}' criado com sucesso!")
else:
    print(f"Superusuário '{username}' já existe.")
