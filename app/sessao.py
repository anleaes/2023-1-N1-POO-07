def __init__(self, id_sessao, filme, sala, horario):
    self._id_sessao = id_sessao
    self._filme = filme
    self._sala = sala
    self._horario = horario
    self._ingressos_vendidos = []

def get_id_sessao(self):
    return self._id_sessao

def set_id_sessao(self, id_sessao):
    self._id_sessao = id_sessao

def get_filme(self):
    return self._filme

def set_filme(self, filme):
    self._filme = filme

def get_sala(self):
    return self._sala

def set_sala(self, sala):
    self._sala = sala

def get_horario(self):
    return self._horario

def set_horario(self, horario):
    self._horario = horario

def get_ingressos_vendidos(self):
    return self._ingressos_vendidos

def adicionar_ingresso_vendido(self, ingresso):
    self._ingressos_vendidos.append(ingresso)

def remover_ingresso_vendido(self, ingresso):
    self._ingressos_vendidos.remove(ingresso)
    