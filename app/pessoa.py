class Pessoa :
    def __init__(self, id, nome, sobrenome, cpf, idade, data_nascimento):
        self._id = id
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._idade = idade
        self._data_nascimento = data_nascimento
    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_sobrenome(self):
        return self._sobrenome
    def get_cpf(self):
        return self._cpf
    def get_idade(self):
        return self._idade
    def get_data_nascimento(self):
        return self._data_nascimento
