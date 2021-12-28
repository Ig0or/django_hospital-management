from ..models import Paciente

def cadastrar_paciente(paciente):
    Paciente.objects.create(nome=paciente.nome, data_nascimento=paciente.data_nascimento, email=paciente.email, telefone=paciente.telefone, cpf=paciente.cpf, profissao=paciente.profissao, endereco=paciente.endereco)