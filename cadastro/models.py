from django.db import models
import datetime

class Tipo_status(models.Model):
    tipo_status = models.CharField('Situação', max_length=50)

    def __str__(self):
        return str(self.tipo_status)

class Empresa(models.Model):
    codigo = models.PositiveIntegerField('Código', default=0, null=True, blank=True)
    razao = models.CharField('Razão/Nome', max_length=200)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=200, default='', null=True, blank=True)
    num = models.CharField('Número', default='', max_length=5, null=True, blank=True)
    cep = models.CharField('CEP', max_length=9, default='', null=True, blank=True)
    data = models.DateTimeField(default=datetime.datetime.now)
    cnpj = models.CharField('CNPJ/CPF', max_length=14, null=True, blank=True )
    ie = models.CharField('Inscrição Estadual', max_length=12, null=True, blank=True)
    im = models.CharField('Inscrição Municipal', max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    status = models.ForeignKey(Tipo_status, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo).rjust(4,'0') + ' - ' + self.razao

    class Meta:
        ordering = ["razao"]

