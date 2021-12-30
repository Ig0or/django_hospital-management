from django.shortcuts import render, redirect
from ..forms import paciente_forms, endereco_forms
from ..services import cep_service, endereco_service, paciente_service
from ..entidades import endereco, paciente

def cadastrar_paciente(request):
    if request.method == 'POST':
        cep_input = request.POST['cep']
        dados_cep = cep_service.consulta_cep(cep_input)

        form_paciente = paciente_forms.Paciente(request.POST)
        form_endereco = endereco_forms.Endereco(request.POST)

        if form_paciente.is_valid():
            nome = form_paciente.cleaned_data['nome']
            data_nascimento = form_paciente.cleaned_data['data_nascimento']
            email = form_paciente.cleaned_data['email']
            telefone = form_paciente.cleaned_data['telefone']
            cpf = form_paciente.cleaned_data['cpf']
            profissao = form_paciente.cleaned_data['profissao']
            if form_endereco.is_valid():
                cep = form_endereco.cleaned_data['cep']
                rua = form_endereco.cleaned_data['rua']
                bairro = form_endereco.cleaned_data['bairro']
                cidade = form_endereco.cleaned_data['cidade']
                estado = form_endereco.cleaned_data['estado']
                numero = form_endereco.cleaned_data['numero']
                complemento = form_endereco.cleaned_data['complemento']

                endereco_novo = endereco.Endereco(cep=cep, rua=rua, bairro=bairro, cidade=cidade, estado=estado, numero=numero, complemento=complemento)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)

                paciente_novo = paciente.Paciente(nome=nome, data_nascimento=data_nascimento, email=email, telefone=telefone, cpf=cpf, profissao=profissao, endereco=endereco_bd)
                paciente_service.cadastrar_paciente(paciente_novo)
                return redirect('lista_pacientes')
    else:
        form_paciente = paciente_forms.Paciente()
        form_endereco = endereco_forms.Endereco()
        dados_cep = ''
    return render(request, 'paciente/form_paciente.html', {'form_paciente': form_paciente, 'form_endereco': form_endereco, 'dados_cep': dados_cep})


def editar_paciente(request, id):
    if request.method == 'POST':
        cep_input = request.POST['cep']
        dados_cep = cep_service.consulta_cep(cep_input)

        paciente_editar = paciente_service.listar_paciente_id(id)
        paciente_editar.data_nascimento = paciente_editar.data_nascimento.strftime('%Y-%m-%d')

        form_paciente = paciente_forms.Paciente(instance=paciente_editar)
        form_endereco = endereco_forms.Endereco(instance=paciente_editar.endereco)

        form_paciente_novo = paciente_forms.Paciente(request.POST)
        form_endereco_novo = endereco_forms.Endereco(request.POST)

        if form_paciente_novo.is_valid() and form_endereco_novo.is_valid():
            nome = form_paciente_novo.cleaned_data['nome']
            data_nascimento = form_paciente_novo.cleaned_data['data_nascimento']
            email = form_paciente_novo.cleaned_data['email']
            telefone = form_paciente_novo.cleaned_data['telefone']
            cpf = form_paciente_novo.cleaned_data['cpf']
            profissao = form_paciente_novo.cleaned_data['profissao']
            cep = form_endereco_novo.cleaned_data['cep']
            rua = form_endereco_novo.cleaned_data['rua']
            bairro = form_endereco_novo.cleaned_data['bairro']
            cidade = form_endereco_novo.cleaned_data['cidade']
            estado = form_endereco_novo.cleaned_data['estado']
            numero = form_endereco_novo.cleaned_data['numero']
            complemento = form_endereco_novo.cleaned_data['complemento']

            endereco_novo = endereco.Endereco(cep=cep, rua=rua, bairro=bairro, cidade=cidade, estado=estado, numero=numero, complemento=complemento)
            endereco_bd = endereco_service.editar_endereco(paciente_editar.endereco, endereco_novo)
        
            paciente_novo = paciente.Paciente(nome=nome, data_nascimento=data_nascimento, email=email, telefone=telefone, cpf=cpf, profissao=profissao, endereco=endereco_bd)
            paciente_service.editar_paciente(paciente_editar, paciente_novo)
            return redirect('lista_pacientes')
    else:
        paciente_editar = paciente_service.listar_paciente_id(id)
        paciente_editar.data_nascimento = paciente_editar.data_nascimento.strftime('%Y-%m-%d')

        form_paciente = paciente_forms.Paciente(instance=paciente_editar)
        form_endereco = endereco_forms.Endereco(instance=paciente_editar.endereco)
        dados_cep = ''
    return render(request, 'paciente/form_paciente.html', {'form_paciente': form_paciente, 'form_endereco': form_endereco, 'dados_cep': dados_cep})


def listar_pacientes(request):
    pacientes = paciente_service.listar_pacientes()
    return render(request, 'paciente/lista_pacientes.html', {'pacientes': pacientes})


def listar_paciente_id(request, id):
    paciente = paciente_service.listar_paciente_id(id)
    return render(request, 'paciente/lista_paciente.html', {'paciente': paciente})


def remover_paciente(request, id):
    paciente = paciente_service.listar_paciente_id(id)
    paciente_service.remover_paciente(paciente)
    return redirect('lista_pacientes')