from django.forms import ModelForm, HiddenInput
from .models import Usuarios
from django.utils.translation import gettext_lazy as _

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['empresa', 'tipo', 'user', 'password', 'cpf', 'cod_acesso', 'descricao']
        widgets = {
            'empresa': HiddenInput
        }
        labels = {
            'empresa': _(''),
        }
        help_texts = {
            'descricao': 'Preencher somente se o campo Tipo = Outros'
        }
