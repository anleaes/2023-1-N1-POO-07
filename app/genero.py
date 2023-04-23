class Genero :

    def __init__(self, nome, descricao) :
        self.nome = nome
        self.descricao = descricao

#   GET e SET do _nome_
    def get_nome(self) :
        return self.nome
    
    def set_nome(self, nome) :
        self._nome = nome

#   GET e SET da _descricao_
    def get_descricao(self) :
        return self.descricao

    def set_descricao(self, descricao) :
        self._descricao = descricao

#   Informações do Gênero
    def genero(self) :
        return "Gênero: " + self.nome + "\n Descrição: " + self.descricao    