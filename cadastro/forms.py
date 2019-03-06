from django.forms import ModelForm
from .models import Empresa

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['codigo', 'razao', 'endereco', 'bairro', 'num', 'cep', 'cnpj', 'ie','im', 'email', 'status']


