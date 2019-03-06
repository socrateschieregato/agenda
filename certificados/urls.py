from django.urls import path
from . import views

urlpatterns = [
    path('certificados/', views.listar_cert_todos, name='listar_cert_todos'),
    path('certificados/<int:empresa_id>', views.listar_certificados, name='listar_certificados'),
    path('novo_certificado/', views.criar_certificado, name='criar_certificado'),
    path('novo_certificado/<int:id>', views.criar_certificado_cliente, name='criar_certificado_cliente'),
    path('update/certificado/<int:id>', views.atualizar_certificado, name='atualizar_certificado'),
    path('delete/certificado/<int:empresa_id>/<int:id>', views.deletar_certificado, name='deletar_certificado'),
]