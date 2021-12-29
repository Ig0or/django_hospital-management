from django.forms import ModelForm
from django.forms.widgets import DateInput, TextInput, EmailInput
from ..models import Paciente

class Paciente(ModelForm):
    class Meta:
        model = Paciente
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
            'profissao': TextInput(
                attrs={'class': 'form-control'}
            ),
        }