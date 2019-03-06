from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('nova_empresa/', views.criar_empresas , name='criar_empresas'),
    path('dados/<int:id>', views.ler , name='ler'),
    path('update/<int:id>', views.atualizar , name='atualizar'),
    path('delete/<int:id>', views.deletar, name='deletar'),
]
