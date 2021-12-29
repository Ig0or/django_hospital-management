from ..models import Endereco

def cadastrar_endereco(endereco):
    return Endereco.objects.create(cep=endereco.cep, rua=endereco.rua, numero=endereco.numero, complemento=endereco.complemento, bairro=endereco.bairro, cidade=endereco.cidade, estado=endereco.estado)

def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.cep = endereco_novo.cep
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.numero = endereco_novo.numero
    endereco_antigo.complemento = endereco_novo.complemento
    endereco_antigo.bairro = endereco_novo.bairro
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.estado = endereco_novo.estado
    endereco_antigo.save(force_update=True)
    return endereco_antigo