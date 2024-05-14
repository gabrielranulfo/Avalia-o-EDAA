import csv
import random
import os
from algoritimos.arvore_binaria import Node
from medidores.medidores import medir_tempo, get_pid, DesvioPadrao, memoria_fim, memoria_inicio, memoria_total_consumida, esperar

def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, "r") as arquivo_aberto:
        for number in arquivo_aberto:
            lista.append(int(number.strip()))  # Convertendo para inteiros
    return lista

diretorio = './arquivos/'
arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    caminho_arquivo = os.path.join(diretorio, arquivo)

    pid = get_pid()

    lista = ler_arquivo(caminho_arquivo)
    
    tamanho_arranjo = len(lista)

    # Instanciando a árvore 
    arvore_binaria = Node(lista[0])

    # Preenche a árvore
    #for x in lista:
    inicio_arvore = medir_tempo()
    inicio_memoria_arvore = memoria_inicio()
    for x in lista:
        if x != lista[0]:
            #print(lista[0])
            #print(x)
            arvore_binaria.insert(x)
            #print(f"Raiz: {arvore_binaria.key} {x}")
        else :
            pass
    fim_arvore = medir_tempo()
    fim_memoria_arvore = memoria_fim()
    print(f"Tempo : {(fim_arvore - inicio_arvore)  * 1e6} (μs) Memória : {memoria_total_consumida(inicio=inicio_memoria_arvore,fim=fim_memoria_arvore)}")
    
    

    '--------- Pior Cenário ---------'

    desvio = DesvioPadrao()
    casos_piores = [-1, -50, -90]
    total_comparacoes_pior = []
    tempos_pior = []
    memoria_pior = []

    for x in casos_piores:
        inicio_memoria_pior = memoria_inicio()
        inicio_tempo_pior = medir_tempo()

        busca,comparacoes =  arvore_binaria.find(value=x,comparison_count=0)    
        total_comparacoes_pior.append(comparacoes)

        fim_tempo_pior = medir_tempo()
        fim_memoria_pior = memoria_fim()

        memoria_pior.append(memoria_total_consumida(inicio=inicio_memoria_pior, fim=fim_memoria_pior))
        tempos_pior.append((fim_tempo_pior - inicio_tempo_pior) * 1e6)

        esperar(segundos=1)
        del inicio_memoria_pior, inicio_tempo_pior, busca,comparacoes, fim_tempo_pior, fim_memoria_pior

    desvio_padrao_resultado_pior = desvio.calcular(total_comparacoes_pior)
    media_comparacoes_pior = desvio.media(total_comparacoes_pior)

    tempo_pior = sum(tempos_pior)
    memoria_consumida_pior = sum(memoria_pior)


    # Salva os resultados em um arquivo CSV
    nome_diretorio = './resultados/'
    if not os.path.exists(nome_diretorio):
        os.makedirs(nome_diretorio)

    nome_arquivo_csv = os.path.join(nome_diretorio, 'busca_arvorebinaria_nao_ordenada.csv')

    with open(nome_arquivo_csv, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        if os.stat(nome_arquivo_csv).st_size == 0:
            escritor_csv.writerow(["Arranjo", "Tipo de Teste", "Média Tempo (μs)", "Desvio Padrão Tempo (μs)", "Média Comparações", "Desvio Padrão Comparações", "Média Memória (bytes)", "Desvio Padrão Memória (bytes)"])

        escritor_csv.writerow([tamanho_arranjo, "Pior Cenário", round(desvio.media(tempos_pior)), round(desvio.calcular(tempos_pior)), round(desvio.media(total_comparacoes_pior)), round(desvio.calcular(total_comparacoes_pior)), round(desvio.media(memoria_pior)), round(desvio.calcular(memoria_pior))])
        #escritor_csv.writerow([tamanho_arranjo, "100 Números Aleatórios", round(desvio.media(tempos_aleatorio)), round(desvio.calcular(tempos_aleatorio)), round(desvio.media(total_comparacoes_aleatorio)), round(desvio.calcular(total_comparacoes_aleatorio)), round(desvio.media(memoria_aleatorio)), round(desvio.calcular(memoria_aleatorio))])

    print("Novos resultados adicionados com sucesso no arquivo:", nome_arquivo_csv)

    # Liberando a memória
    #del desvio, casos_piores, total_comparacoes_pior, tempos_pior, memoria_pior, total_comparacoes_aleatorio, tempos_aleatorio, memoria_aleatorio, numeros_aleatorios


    esperar(segundos=5)


print("Testes Finalizados!!")
