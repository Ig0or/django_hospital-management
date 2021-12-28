from django.forms import ModelForm
from django.forms.widgets import DateInput
from ..models import Paciente

class Paciente(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('endereco', )
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            ),
        }