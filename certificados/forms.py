from django.forms import ModelForm, HiddenInput, TextInput
from .models import Certificados
from django.utils.translation import gettext_lazy as _


class CertificadosForm(ModelForm):
    class Meta:
        model = Certificados
        fields = ['empresa', 'tipo', 'validade', 'email', 'password', 'name']
        widgets = {
            'empresa': HiddenInput
        }
        labels = {
            'empresa': _(''),
        }

class CertificadoForm(ModelForm):
    class Meta:
        model = Certificados
        fields = ['empresa', 'tipo', 'validade', 'email', 'password', 'name']