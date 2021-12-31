from django.shortcuts import redirect, render
from ..services import cep_service, endereco_service, funcionario_service
from ..forms import funcionario_forms, endereco_forms
from ..entidades import endereco, funcionario

def cadastrar_funcionario(request):
    if request.method == 'POST':
        cep_input = request.POST['cep']
        dados_cep = cep_service.consulta_cep(cep_input)

        form_funcionario = funcionario_forms.Funcionario(request.POST)
        form_endereco = endereco_forms.Endereco(request.POST)

        if form_funcionario.is_valid() and form_endereco.is_valid():
            nome = form_funcionario.cleaned_data['nome']
            data_nascimento = form_funcionario.cleaned_data['data_nascimento']
            email = form_funcionario.cleaned_data['email']
            telefone = form_funcionario.cleaned_data['telefone']
            cpf = form_funcionario.cleaned_data['cpf']
            tipo_funcionario = form_funcionario.cleaned_data['tipo_funcionario']
            cep = form_endereco.cleaned_data['cep']
            rua = form_endereco.cleaned_data['rua']
            bairro = form_endereco.cleaned_data['bairro']
            cidade = form_endereco.cleaned_data['cidade']
            estado = form_endereco.cleaned_data['estado']
            numero = form_endereco.cleaned_data['numero']
            complemento = form_endereco.cleaned_data['complemento']

            endereco_novo = endereco.Endereco(cep=cep, rua=rua, bairro=bairro, cidade=cidade, estado=estado, numero=numero, complemento=complemento)
            endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)

            funcionario_novo = funcionario.Funcionario(nome=nome, data_nascimento=data_nascimento, email=email, telefone=telefone, cpf=cpf, tipo_funcionario=tipo_funcionario, endereco=endereco_bd)
            funcionario_service.cadastrar_funcionario(funcionario_novo)
            return redirect('lista_pacientes')
    else:
        form_funcionario = funcionario_forms.Funcionario()
        form_endereco = endereco_forms.Endereco()
        dados_cep = ''
    return render(request, 'funcionario/form_funcionario.html', {'form_funcionario': form_funcionario, 'form_endereco': form_endereco, 'dados_cep': dados_cep})