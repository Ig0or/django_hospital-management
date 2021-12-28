from django.shortcuts import render, redirect
from ..forms import paciente_forms, endereco_forms
from ..services import cep_service

def cadastrar_paciente(request):
    if request.method == 'POST':
        cep = request.POST['cep']
        dados_cep = cep_service.consulta_cep(cep)
        form_paciente = paciente_forms.Paciente(request.POST)
        form_endereco = endereco_forms.Endereco(request.POST)
        print(form_endereco)
    else:
        form_paciente = paciente_forms.Paciente()
        form_endereco = endereco_forms.Endereco()
        dados_cep = ''
    return render(request, 'paciente/form_paciente.html', {'form_paciente': form_paciente, 'form_endereco': form_endereco, 'dados_cep': dados_cep})

