from django.forms import ModelForm
from django.forms.widgets import TextInput, DateInput, EmailInput, Select
from ..models import Funcionario

class Funcionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        exclude = ('endereco', )
        widgets = {
            'nome': TextInput(
                attrs={'class': 'form-control'}
            ),
            'cpf': TextInput(
                attrs={'class': 'form-control'}
            ),
            'data_nascimento': DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'email': EmailInput(
                attrs={'class': 'form-control'}
            ),
            'telefone': TextInput(
                attrs={'class': 'form-control'}
            ),
            'tipo_funcionario': Select(
                attrs={'class': 'form-control'}
            ),
        }