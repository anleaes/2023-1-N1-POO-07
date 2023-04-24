class Categoria :
    
    def __init__(self, titulo_categoria, descricao_categoria) :
        self._titulo_categoria = titulo_categoria
        self._descricao_categoria = descricao_categoria

#   GET e SET do _titulo_
    def get_tituloCategoria(self) :
        return self._titulo_categoria
    
    def set_tituloCategoria(self, titulo_categoria) :
        self._titulo_categoria = titulo_categoria

#   GET e SET da _descricao_
    def get_descricaoCategoria(self) :
        return self._descricao_categoria

    def set_descricaoCategoria(self, descricao) :
        self._descricao_categoria = descricao_categoria


#   Informações da Categoria
    def categoria(self) :
        return "Categoria: " + self._titulo_categoria + "\n Descrição: " + self._descricao_categoria
    