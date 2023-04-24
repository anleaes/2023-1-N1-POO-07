class Genero :

    def __init__(self, nome_genero, descricao_genero) :
        self._nome_genero = nome_genero
        self._descricao_genero = descricao_genero

#   GET e SET do _nome_
    def get_nomeGenero(self) :
        return self._nome_genero
    
    def set_nomeGenero(self, nome_genero) :
        self._nome_genero = nome_genero

#   GET e SET da _descricao_
    def get_descricaoGenero(self) :
        return self._descricao_genero

    def set_descricaoGenero(self, descricao_genero) :
        self._descricao_genero = descricao_genero

#   Informações do Gênero
    def genero(self) :
        return "Gênero: " + self._nome_genero + "\n Descrição: " + self._descricao_genero    