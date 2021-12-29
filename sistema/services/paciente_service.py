from ..models import Paciente


def cadastrar_paciente(paciente):
    Paciente.objects.create(nome=paciente.nome, data_nascimento=paciente.data_nascimento, email=paciente.email, telefone=paciente.telefone, cpf=paciente.cpf, profissao=paciente.profissao, endereco=paciente.endereco)


def listar_pacientes():
    return Paciente.objects.all()


def listar_paciente_id(id):
    return Paciente.objects.get(id=id)