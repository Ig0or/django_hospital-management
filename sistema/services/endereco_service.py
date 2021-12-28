from ..models import Endereco

def cadastrar_endereco(endereco):
    return Endereco.objects.create(cep=endereco.cep, rua=endereco.rua, numero=endereco.numero, complemento=endereco.complemento, bairro=endereco.bairro, cidade=endereco.cidade, estado=endereco.estado)