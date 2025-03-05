from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticação
    path('auth/', include('autenticacao.urls')),

    # APIs do sistema
    path('api/', include('compras.urls')),  # Compras
    path('api/', include('feiras.urls')),   # Feiras
    path('api/', include('estoque.urls')),   # Estoque
    path('api/', include('credito.urls')),   # Crédito
    path('api/', include('financeiro.urls')),   # Financeiro
]
