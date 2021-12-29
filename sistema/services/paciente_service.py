from ..models import Paciente


def cadastrar_paciente(paciente):
    Paciente.objects.create(nome=paciente.nome, data_nascimento=paciente.data_nascimento, email=paciente.email, telefone=paciente.telefone, cpf=paciente.cpf, profissao=paciente.profissao, endereco=paciente.endereco)


def editar_paciente(paciente_antigo, paciente_novo):
    paciente_antigo.nome = paciente_novo.nome
    paciente_antigo.data_nascimento = paciente_novo.data_nascimento
    paciente_antigo.email = paciente_novo.email
    paciente_antigo.telefone = paciente_novo.telefone
    paciente_antigo.cpf = paciente_novo.cpf
    paciente_antigo.profissao = paciente_novo.profissao
    paciente_antigo.endereco = paciente_novo.endereco
    paciente_antigo.save(force_update=True)

def listar_pacientes():
    return Paciente.objects.all()


def listar_paciente_id(id):
    return Paciente.objects.get(id=id)