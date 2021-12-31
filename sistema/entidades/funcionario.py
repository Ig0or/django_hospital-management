class Funcionario():
    def __init__(self, nome, data_nascimento, email, telefone, cpf, tipo_funcionario, endereco):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__telefone = telefone
        self.__cpf = cpf
        self.__tipo_funcionario = tipo_funcionario
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def tipo_funcionario(self):
        return self.__tipo_funcionario

    @tipo_funcionario.setter
    def tipo_funcionario(self, tipo_funcionario):
        self.__tipo_funcionario = tipo_funcionario

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
