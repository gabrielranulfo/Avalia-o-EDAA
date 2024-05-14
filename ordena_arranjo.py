import csv
import random
import os
from medidores.medidores import medir_tempo, get_pid, DesvioPadrao, memoria_fim, memoria_inicio, memoria_total_consumida, esperar

def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, "r") as arquivo_aberto:
        for number in arquivo_aberto:
            lista.append(int(number.strip()))  # Convertendo para inteiros
    
    inicio_tempo_ordenacao = medir_tempo()
    inicio_memoria_ordenacao = memoria_inicio()


    lista.sort()   

    
    fim_memoria_ordenacao = memoria_fim()
    fim_tempo_ordenacao = medir_tempo()

    memoria_ordenacao = memoria_total_consumida(inicio=inicio_memoria_ordenacao, fim=fim_memoria_ordenacao)
    tempos_ordenacao = ((fim_tempo_ordenacao - inicio_tempo_ordenacao) * 1e6)
    
    
    return lista, tempos_ordenacao, memoria_ordenacao

diretorio = './arquivos/'
arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    nome = arquivo
    caminho_arquivo = os.path.join(diretorio, arquivo)

    pid = get_pid()


    lista, tempos_ordenacao, memoria_ordenacao = ler_arquivo(caminho_arquivo)

    tamanho_arranjo = len(lista)

    novo_nome = os.path.join("./arquivos_ordenados/", nome)

    with open(novo_nome, "w") as f:
        for number in lista:
            f.write(str(number) + "\n")

    nome_arquivo_csv = "./resultados/tempos_ordenacao.csv"

    with open(nome_arquivo_csv, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        if os.stat(nome_arquivo_csv).st_size == 0:
            escritor_csv.writerow([
                "Arranjo",
                "Arquivo", 
                "Tempo de Ordenação (μs)", 
                "Memória (bytes)", 
                ])

        escritor_csv.writerow([tamanho_arranjo,caminho_arquivo,round(tempos_ordenacao) ,memoria_ordenacao])
    print(f"Arquivo {nome_arquivo_csv} salvo com sucesso.")