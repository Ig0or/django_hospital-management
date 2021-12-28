from django.forms import ModelForm
from ..models import Paciente

class Paciente(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('endereco', )