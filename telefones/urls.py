from django.urls import path
from . import views

urlpatterns = [
    path('telefones/<int:empresa_id>', views.listar_telefones, name='listar_telefones'),
    path('novo_telefone/<int:id>', views.criar_telefones , name='criar_telefones'),
    path('update/telefones/<int:id>', views.atualizar_telefones , name='atualizar_telefones'),
    path('delete/telefone/<int:empresa_id>/<int:id>', views.deletar_telefones, name='deletar_telefones'),
]