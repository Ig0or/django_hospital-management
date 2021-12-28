from django.forms import ModelForm
from ..models import Endereco

class Endereco(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
