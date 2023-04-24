def __init__(self, id_sala, capacidade, tipo):
    self._id_sala = id_sala
    self._capacidade = capacidade
    self._tipo = tipo
    self._sessoes = []

def get_id_sala(self):
    return self._id_sala

def set_id_sala(self, id_sala):
    self._id_sala = id_sala

def get_capacidade(self):
    return self._capacidade

def set_capacidade(self, capacidade):
    self._capacidade = capacidade

def get_tipo(self):
    return self._tipo

def set_tipo(self, tipo):
    self._tipo = tipo

def get_sessoes(self):
    return self._sessoes

def adicionar_sessao(self, sessao):
    self._sessoes.append(sessao)

def remover_sessao(self, sessao):
    self._sessoes.remove(sessao)
    