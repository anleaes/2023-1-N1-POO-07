class Categoria :
    
    def __init__(self, titulo, descricao) :
        self.titulo = titulo
        self.descricao = descricao

#   GET e SET do _titulo_
    def get_titulo(self) :
        return self.titulo
    
    def set_titulo(self, titulo) :
        self._titulo = titulo

#   GET e SET da _descricao_
    def get_descricao(self) :
        return self.descricao

    def set_descricao(self, descricao) :
        self._descricao = descricao


#   Informações da Categoria
    def categoria(self) :
        return "Categoria: " + self.titulo + "\n Descrição: " + self.descricao
    