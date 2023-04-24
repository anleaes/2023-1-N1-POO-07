class IngressoCinema :
    def __init__(self, nome_filme, horario, preco_base):
        self._nome_filme = nome_filme
        self._horario = horario
        self._preco_base = preco_base
   
    def calcular_preco(self):
        return self._preco_base
   
    def imprimir_ingresso(self):
        print("---- Ingresso de cinema ----")
        print("Filme:", self._nome_filme)
        print("Horário:", self._horario)
        print("Preço:", self.calcular_preco())
