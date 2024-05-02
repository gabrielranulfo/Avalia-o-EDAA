import time
import psutil
import os
import tracemalloc

def get_pid():
    pid = os.getpid()
    return pid

def memoria_processo():
    processo = psutil.Process(get_pid())
    memoria_utilizada = processo.memory_info().rss
    return memoria_utilizada

def memoria_total(inicio,fim):
    return inicio - fim
  
def medir_tempo():
    return time.time()

def tempo_total(inicio,fim):
    return fim - inicio

def memoria_inicio():
    tracemalloc.start()
    inicio = tracemalloc.take_snapshot()
    return inicio

def memoria_fim():
    fim = tracemalloc.take_snapshot()
    tracemalloc.stop()
    return fim
    
def memoria_total_consumida(inicio,fim):
    diferenca = fim.compare_to(inicio, 'lineno')
    estatisticas = diferenca
    tamanho_total_alocado = 0
    tamanho_total_liberado = 0

    # Percorra a lista de estatísticas de diferença
    for estatistica in estatisticas:
        # Verifique se o tamanho da estatística é positivo ou negativo
        if estatistica.size > 0:
            # Se positivo, é uma alocação, então adicione ao tamanho total alocado
            tamanho_total_alocado += estatistica.size
        else:
            # Se negativo, é uma liberação, então adicione ao tamanho total liberado
            tamanho_total_liberado += abs(estatistica.size)

    # Calcule a diferença líquida entre o tamanho total alocado e o total liberado
    diferenca_memoria = tamanho_total_alocado - tamanho_total_liberado
    return diferenca_memoria

class DesvioPadrao:
    def __init__(self):
        pass

    def media(self, data):
        return sum(data) / len(data)

    def variancia(self, data):
        mu = self.media(data)
        return sum((x - mu) ** 2 for x in data) / len(data)

    def calcular(self, data):
        return self.variancia(data) ** 0.5

