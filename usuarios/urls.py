from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/<int:empresa_id>', views.listar_user, name='listar_user'),
    path('novo_usuario/<int:id>', views.criar_user, name='criar_user'),
    path('update/usuario/<int:id>', views.atualizar_user, name='atualizar_user'),
    path('delete/user/<int:empresa_id>/<int:id>', views.deletar_user, name='deletar_user'),
]