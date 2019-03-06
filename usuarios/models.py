from django.db import models
from cadastro.models import Empresa

class Tipo_usuario(models.Model):
    tipo_usuario = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tipo_usuario)

class Usuarios(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)
    user = models.CharField('Usuário', default='', max_length=30, null=True, blank=True)
    password = models.CharField('Senha', default='', max_length=30, null=True, blank=True)
    descricao = models.CharField('Descrição', default='', max_length=30, null=True, blank=True)
    cpf = models.CharField('CPF/CNPJ', default='', max_length=30, null=True, blank=True)
    cod_acesso = models.CharField('Código Acesso(RFB)', default='', max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.user)
