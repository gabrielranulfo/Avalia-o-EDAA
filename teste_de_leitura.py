from ler_arquivo import ler_arquivo
from lista_ligada import Node,LinkedList
from medidores import memoria_processo,memoria_total, tempo_total,medir_tempo, get_pid,esperar,memoria_inicio,memoria_fim
import random

pid = get_pid()

nome_arquivo = './arranjo_800_mil.txt'
lista = ler_arquivo(nome_arquivo)
lista_ligada = LinkedList()


'------Preencher Lista Ligada------'
#inicio_tempo = medir_tempo()
#inicio_memoria = memoria_processo()

for x in lista:
    lista_ligada.append(x)

#fim_tempo = medir_tempo()
#fim_memoria = memoria_processo()


#memoria_consumida = fim_memoria - inicio_memoria
#tempo = tempo_total(inicio=inicio_tempo,fim=fim_tempo)

#print("-" * 70)
#print("Estatisticas de Preenchimento")
#print("-" * 70)
#print("PID do processo atual:", pid)
#print(f"Tempo : {round(tempo, 9):.4f} seg")
#print(f"Memória consumida pelo processo: {memoria_consumida / 1024} KB")

#del inicio_tempo,inicio_memoria,fim_tempo,fim_memoria,memoria_consumida,tempo
#esperar()
#lista_ligada.print_list()

'------Ordenar Lista Ligada------'

lista.sort()

#inicio_tempo = medir_tempo()
#inicio_memoria = memoria_processo()
#lista_ligada.ordenar_lista_ligada()
#fim_tempo = medir_tempo()
#memoria_consumida = fim_memoria - inicio_memoria
#tempo = tempo_total(inicio=inicio_tempo,fim=fim_tempo)
#
#print("-" * 70)
#print("Estatisticas da Ordenação")
#print("-" * 70)
#print("PID do processo atual:", pid)
#print(f"Tempo : {round(tempo, 9):.4f} seg")
#print(f"Memória consumida pelo processo: {memoria_consumida / 1024} KB")
#print(f"Memória Inicial : {inicio_memoria/1024} KB")
#print(f"Memória Final : {fim_memoria/1024} KB")
#
#del inicio_tempo,inicio_memoria,fim_tempo,fim_memoria,memoria_consumida,tempo
#esperar()

#lista_ligada.print_list()

'------Pior Cenário------'

print("-" * 70)
print("Estatisticas dos Testes de Pior Cenário")
print("-" * 70)
#1º teste
#ordenacao = True

inicio_tempo = medir_tempo()
inicio_memoria = memoria_processo()
#i = memoria_inicio()

lista_ligada.comparacoes_totais = 0
lista_ligada.busca_sequencial_lista_ligada(valor=-1)
print(f"Comparações 1: {lista_ligada.comparacoes_totais}")

#2º teste

lista_ligada.comparacoes_totais = 0
lista_ligada.busca_sequencial_lista_ligada(valor=-50)
print(f"Comparações 2: {lista_ligada.comparacoes_totais}")

#3º Teste

lista_ligada.comparacoes_totais = 0
lista_ligada.busca_sequencial_lista_ligada(valor=99999954)
print(f"Comparações 3: {lista_ligada.comparacoes_totais}")

fim_tempo = medir_tempo()
fim_memoria = memoria_processo()
#f = memoria_fim()


memoria_consumida = fim_memoria - inicio_memoria
tempo = tempo_total(inicio=inicio_tempo,fim=fim_tempo)
#memoria_consumida2 = memoria_total_consumida(inicio=i,fim=f)

print("-" * 70)
print("PID do processo atual:", pid)
print(f"Tempo : {round(tempo, 9):.4f} seg")
print(f"Memória consumida pelo processo: {memoria_consumida / 1024} KB")
print(f"Memória Inicial : {inicio_memoria/1024} KB")
print(f"Memória Final : {fim_memoria/1024} KB")

'''
print("-" * 70)
print("FUNÇÃO DE MEMÓRIA NOVA !!")
print("Estatisticas dos Testes de Pior Cenário")
print("-" * 70)
print("PID do processo atual:", pid)
print(f"Tempo : {round(tempo, 9):.4f} seg")
print(f"Memória consumida pelo processo: {memoria_consumida2 / 1024} KB")'''

'------100 Números Aleatórios------'
numeros_aleatorios = random.sample(lista, 100)

inicio_tempo = medir_tempo()
inicio_memoria = memoria_processo()
i = memoria_inicio()

for x in numeros_aleatorios:
    lista_ligada.busca_sequencial_lista_ligada(valor=x)

fim_tempo = medir_tempo()
fim_memoria = memoria_processo()
f = memoria_fim()


memoria_consumida = fim_memoria - inicio_memoria
tempo = tempo_total(inicio=inicio_tempo,fim=fim_tempo)
#memoria_consumida2 = memoria_total_consumida(inicio=i,fim=f)

print("-" * 70)
print("Estatisticas dos 100 Números Aleatórios")
print("-" * 70)
print("PID do processo atual:", pid)
print(f"Tempo : {round(tempo, 9):.4f} seg")
print(f"Memória consumida pelo processo: {memoria_consumida /1024} KB")
print(f"Comparações : {lista_ligada.comparacoes_totais}")
print(f"Memória Inicial : {inicio_memoria/1024} KB")
print(f"Memória Final : {fim_memoria/1024} KB")
'''
print("-" * 70)
print("FUNÇÃO DE MEMÓRIA NOVA !!")
print("Estatisticas dos 100 Números Aleatórios")
print("-" * 70)
print("PID do processo atual:", pid)
print(f"Tempo : {round(tempo, 9):.4f} seg")
print(f"Memória consumida pelo processo: {memoria_consumida2 / 1024} KB")
print(f"Comparações : {lista_ligada.comparacoes_totais}")'''