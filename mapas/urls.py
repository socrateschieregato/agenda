from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_planilhas, name='listar_planilhas'),
    path('nova_planilha/', nova_planilha , name='nova_planilha'),
    path('notas/<int:id>', listar_notas , name='listar_notas'),
]