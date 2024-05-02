from ler_arquivo import ler_arquivo
from lista_ligada import Node, LinkedList
from medidores import memoria_processo, memoria_total, tempo_total, medir_tempo, get_pid, esperar, memoria_inicio, memoria_fim
import random

pid = get_pid()

nome_arquivo = './arranjo_800_mil.txt'
lista = ler_arquivo(nome_arquivo)
lista_ligada = LinkedList()

with open("estatisticas.txt", "w") as arquivo:
    '------Preencher Lista Ligada------'
    for x in lista:
        lista_ligada.append(x)

    '------Ordenar Lista Ligada------'
    inicio_tempo = medir_tempo()
    inicio_memoria = memoria_processo()
    for x in lista:
        lista_ligada.append(x)

    fim_tempo = medir_tempo()
    fim_memoria = memoria_processo()

    memoria_consumida = fim_memoria - inicio_memoria
    tempo = tempo_total(inicio=inicio_tempo, fim=fim_tempo)

    print("-" * 70, file=arquivo)
    print("Estatisticas da Ordenação", file=arquivo)
    print("-" * 70, file=arquivo)
    print("PID do processo atual:", pid, file=arquivo)
    print(f"Tempo : {round(tempo, 9):.4f} seg", file=arquivo)
    print(f"Memória consumida pelo processo: {memoria_consumida / 1024} KB", file=arquivo)
    print(f"Memória Inicial : {inicio_memoria/1024} KB", file=arquivo)
    print(f"Memória Final : {fim_memoria/1024} KB", file=arquivo)

    '------Pior Cenário------'
    print("-" * 70, file=arquivo)
    print("Estatisticas dos Testes de Pior Cenário", file=arquivo)
    print("-" * 70, file=arquivo)
    inicio_tempo = medir_tempo()
    inicio_memoria = memoria_processo()
    i = memoria_inicio()

    lista_ligada.comparacoes_totais = 0
    lista_ligada.busca_sequencial_lista_ligada(valor=-1)
    print(f"Comparações 1: {lista_ligada.comparacoes_totais}", file=arquivo)

    lista_ligada.comparacoes_totais = 0
    lista_ligada.busca_sequencial_lista_ligada(valor=-50)
    print(f"Comparações 2: {lista_ligada.comparacoes_totais}", file=arquivo)

    lista_ligada.comparacoes_totais = 0
    lista_ligada.busca_sequencial_lista_ligada(valor=99999954)
    print(f"Comparações 3: {lista_ligada.comparacoes_totais}", file=arquivo)

    fim_tempo = medir_tempo()
    fim_memoria = memoria_processo()
    f = memoria_fim()

    memoria_consumida = fim_memoria - inicio_memoria
    tempo = tempo_total(inicio=inicio_tempo, fim=fim_tempo)

    print("-" * 70, file=arquivo)
    print("PID do processo atual:", pid, file=arquivo)
    print(f"Tempo : {round(tempo, 9):.4f} seg", file=arquivo)
    print(f"Memória consumida pelo processo: {memoria_consumida / 1024} KB", file=arquivo)
    print(f"Memória Inicial : {inicio_memoria/1024} KB", file=arquivo)
    print(f"Memória Final : {fim_memoria/1024} KB", file=arquivo)

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
    tempo = tempo_total(inicio=inicio_tempo, fim=fim_tempo)

    print("-" * 70, file=arquivo)
    print("Estatisticas dos 100 Números Aleatórios", file=arquivo)
    print("-" * 70, file=arquivo)
    print("PID do processo atual:", pid, file=arquivo)
    print(f"Tempo : {round(tempo, 9):.4f} seg", file=arquivo)
    print(f"Memória consumida pelo processo: {memoria_consumida /1024} KB", file=arquivo)
    print(f"Comparações : {lista_ligada.comparacoes_totais}", file=arquivo)
    print(f"Memória Inicial : {inicio_memoria/1024} KB", file=arquivo)
    print(f"Memória Final : {fim_memoria/1024} KB", file=arquivo)
