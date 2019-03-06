from django.db import models
from cadastro.models import Empresa, Tipo_status


class Tipo_certificado(models.Model):
    tipo_certificado = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tipo_certificado)

class Certificados(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_certificado, on_delete=models.CASCADE)
    email = models.EmailField('Email da Compra', max_length=254, null=True, blank=True)
    validade = models.DateField('Validade')
    password = models.CharField('Senha', default='', max_length=30)
    status = models.ForeignKey(Tipo_status, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Nome', default='', max_length=60, null=True, blank=True)

    def __str__(self):
        return str(self.empresa) + ' ' + str(self.tipo)