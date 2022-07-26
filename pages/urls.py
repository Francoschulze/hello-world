from django.urls import path
from .views import home_page_view


urlpatterns = [
    path('', home_page_view, name='home'),
]
"""
Nosso padrão de URL tem três partes:
    - Uma expressão regular Python para string vazia;
    - Uma referência à view chamada home_page_view;
    - Um padrão de URL nomeado (opcional) chamado 'home'.
"""