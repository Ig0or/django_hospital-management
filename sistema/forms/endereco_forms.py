from django.forms import ModelForm, widgets
from django.forms.widgets import TextInput
from ..models import Endereco

class Endereco(ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado']
        widgets = {
            'cep': TextInput(
                attrs={'class': 'form-control'}
            ),
            'rua': TextInput(
                attrs={'class': 'form-control'}
            ),
            'numero': TextInput(
                attrs={'class': 'form-control'}
            ),
            'complemento': TextInput(
                attrs={'class': 'form-control'}
            ),
            'bairro': TextInput(
                attrs={'class': 'form-control'}
            ),
            'cidade': TextInput(
                attrs={'class': 'form-control'}
            ),
            'estado': TextInput(
                attrs={'class': 'form-control'}
            ),
        }
