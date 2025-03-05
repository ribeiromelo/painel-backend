from django.urls import path
from .views import DespesaListCreateView

urlpatterns = [
    path("financeiro/", DespesaListCreateView.as_view(), name="financeiro-list"),
]
