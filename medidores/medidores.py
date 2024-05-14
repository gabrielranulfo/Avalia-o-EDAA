import time
import psutil
import os
import tracemalloc

def get_pid():
    pid = os.getpid()
    return pid
  
def medir_tempo():
    return time.perf_counter()

def tempo_total(inicio,fim):
    return fim - inicio

def memoria_inicio():
    #esperar(segundos=0.5)
    process = psutil.Process(get_pid())
    inicio = process.memory_info().rss
    #print(process.memory_maps())
    del process
    return inicio

def memoria_fim():
    #esperar(segundos=0.5)
    process = psutil.Process(get_pid())
    fim = process.memory_info().rss
    #print(process.memory_maps())
    del process
    return fim

    
def memoria_total_consumida(inicio,fim):
    diferenca = fim - inicio
    return (inicio + diferenca) #bytes
    del fim, inicio

def esperar(segundos):
    time.sleep(segundos)

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