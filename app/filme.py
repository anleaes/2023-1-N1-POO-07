from categoria import Categoria
from genero import Genero

class Filme (Categoria, Genero):

    def __init__(self, titulo_categoria, descricao_categoria, nome_genero, descricao_genero, titulo_filme, ano, duracao, descricao_filme, faixa_etaria, diretor, avaliacao_geral) :
        Categoria.__init__(self, titulo_categoria, descricao_categoria)
        Genero.__init__(self, nome_genero, descricao_genero)
        self._titulo_filme = titulo_filme
        self._ano = ano
        self._duracao = duracao
        self._descricao_filme = descricao_filme
        self._faixa_etaria = faixa_etaria
        self._diretor = diretor
        self._avaliacao_geral = avaliacao_geral

#   GET e SET do _titulo-filme_
    def get_tituloFilme(self) :
        return self._titulo_filme
    
    def set_tituloFilme(self, titulo_filme) :
        self._titulo_filme = titulo_filme

#   GET e SET do _ano_
    def get_ano(self) :
        return self._ano
    
    def set_ano(self, ano) :
        self._ano = ano

#   GET e SET da _duracao_
    def get_duracao(self) :
        return self._duracao
    
    def set_tituloFilme(self, duracao) :
        self._duracao = duracao

#   GET e SET da _descricao-filme_
    def get_descricaoFilme(self) :
        return self._descricao_filme
    
    def set_descricaoFilme(self, descricao_filme) :
        self._descricao_filme = descricao_filme

#   GET e SET da _faixa-etaria_
    def get_faixaEtaria(self) :
        return self._faixa_etaria
    
    def set_faixaEtaria(self, faixa_etaria) :
        self._faixa_etaria = faixa_etaria

#   GET e SET do _diretor_
    def get_diretor(self) :
        return self._diretor
    
    def set_diretor(self, diretor) :
        self._diretor = diretor

#   GET e SET da _avaliacao-geral_
    def get_avaliacaoGeral(self) :
        return self._avaliacao_geral
    
    def set_avaliacaoGeral(self, avaliacao_geral) :
        self._avaliacao_geral = avaliacao_geral

#   Mostra a categoria do filme
    def categoriaFilme(self) :
        return self._titulo_categoria

#   Mostra o gênero do filme
    def generoFilme(self) :
        return self._nome_genero