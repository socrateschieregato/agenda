from django.forms import ModelForm, HiddenInput
from .models import Telefones
from django.utils.translation import gettext_lazy as _

class TelefoneForm(ModelForm):
    class Meta:
        model = Telefones
        fields = ['empresa','tipo','num', 'pessoa']
        widgets = {
            'empresa': HiddenInput
        }
        labels = {
            'empresa': _(''),
        }
