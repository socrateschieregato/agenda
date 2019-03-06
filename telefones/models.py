from django.db import models
from cadastro.models import Empresa


class Tipo_telefone(models.Model):
    tipo_telefone = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tipo_telefone)

class Telefones(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_telefone, on_delete=models.CASCADE)
    num = models.CharField('Número', default='', max_length=15,unique=True)
    pessoa = models.CharField('Pessoa', default='', max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.empresa) + ' ' + str(self.num)

