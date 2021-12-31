from django.db import models
from django.db.models.fields.related import ForeignKey

class Endereco(models.Model):
    cep = models.CharField(max_length=8, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=5, null=False, blank=False)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=20, null=False, blank=False)
    cidade = models.CharField(max_length=20, null=False, blank=False)
    estado = models.CharField(max_length=20, null=False, blank=False)


class Paciente(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=11, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    profissao = models.CharField(max_length=30, null=False, blank=False )
    endereco = ForeignKey(Endereco, blank=False, null=False, on_delete=models.CASCADE)


class Funcionario(models.Model):
    FUNCIONARIOS_CHOICES = (
        (1, 'Atendente'),
        (2, 'Médico'),
    )
    nome = models.CharField(max_length=150, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=11, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    tipo_funcionario = models.IntegerField(choices=FUNCIONARIOS_CHOICES, null=False, blank=False)
    endereco = ForeignKey(Endereco, blank=False, null=False, on_delete=models.CASCADE)