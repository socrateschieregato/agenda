from django.forms import ModelForm, HiddenInput
from .models import Fiscal
from django.utils.translation import gettext_lazy as _

class FiscalForm(ModelForm):
    class Meta:
        model = Fiscal
        fields = ['empresa', 'mes', 'ano', 'planilha']

