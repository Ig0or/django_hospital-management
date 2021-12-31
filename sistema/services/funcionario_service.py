from ..models import Funcionario

def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, data_nascimento=funcionario.data_nascimento, email=funcionario.email, telefone=funcionario.telefone, cpf=funcionario.cpf, tipo_funcionario=funcionario.tipo_funcionario, endereco=funcionario.endereco)


def listar_funcionarios():
    return Funcionario.objects.all()