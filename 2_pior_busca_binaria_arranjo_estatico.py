import csv
import random
import os
from algoritimos.arranjo_estatico import ArranjoEstatico
from medidores.medidores import medir_tempo, memoria_inicio, memoria_fim, memoria_total_consumida, DesvioPadrao, esperar


def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, "r") as arquivo_aberto:
        for number in arquivo_aberto:
            lista.append(int(number.strip()))  # Convertendo para inteiros
    return lista


diretorio = './arquivos_ordenados/'
arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    caminho_arquivo = os.path.join(diretorio, arquivo)

    lista = ler_arquivo(caminho_arquivo)
    tamanho_arranjo = len(lista)

    # Instanciando o arranjo estático
    arranjo_estatico = ArranjoEstatico(tamanho_arranjo)

    # Preenche o arranjo estático
    inicio_arranjo = medir_tempo()
    inicio_memoria_arranjo = memoria_inicio()
    for i, valor in enumerate(lista):
        arranjo_estatico.inserir(valor, i)
    fim_arranjo = medir_tempo()
    fim_memoria_arranjo = memoria_fim()

    print(f"Arranjo {arquivo} Tempo : {(fim_arranjo - inicio_arranjo)  * 1e6} (μs) Memória : {memoria_total_consumida(inicio=inicio_memoria_arranjo,fim=fim_memoria_arranjo)}")


    '--------- Pior Cenário ---------'
    desvio = DesvioPadrao()

    casos_piores = [-1, -50, -90]
    total_comparacoes_pior = []
    tempos_pior = []
    memoria_pior = []

    for x in casos_piores:
        inicio_tempo_pior = medir_tempo()
        inicio_memoria_pior = memoria_inicio()

        arranjo_estatico.buscar_binaria(x)
        total_comparacoes_pior.append(arranjo_estatico.comparacoes_totais)

        fim_tempo_pior = medir_tempo()
        fim_memoria_pior = memoria_fim()

        memoria_pior.append(memoria_total_consumida(inicio=inicio_memoria_pior, fim=fim_memoria_pior))
        tempos_pior.append((fim_tempo_pior - inicio_tempo_pior) * 1e6)
        arranjo_estatico.comparacoes_totais = 0
        esperar(segundos=1)
        del inicio_tempo_pior,inicio_memoria_pior,fim_tempo_pior,fim_memoria_pior

    desvio_padrao_resultado_pior = desvio.calcular(total_comparacoes_pior)
    media_comparacoes_pior = desvio.media(total_comparacoes_pior)

    # Salva os resultados em um arquivo CSV
    nome_diretorio = './resultados/'
    if not os.path.exists(nome_diretorio):
        os.makedirs(nome_diretorio)

    nome_arquivo_csv = os.path.join(nome_diretorio, 'busca_binaria_arranjo_estatico_ordenado.csv')

    with open(nome_arquivo_csv, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Escreve cabeçalhos apenas se o arquivo não existir
        if os.stat(nome_arquivo_csv).st_size == 0:
            escritor_csv.writerow(["Arranjo", "Tipo de Teste", "Média Tempo (μs)", "Desvio Padrão Tempo (μs)", "Média Comparações","Desvio Padrão Comparações", "Média Memória (bytes)", "Desvio Padrão Memória (bytes)"])

        # Adiciona os dados dos testes
        escritor_csv.writerow([tamanho_arranjo, "Pior Cenário", round(desvio.media(tempos_pior)), round(desvio.calcular(tempos_pior)), round(desvio.media(total_comparacoes_pior)), round(desvio.calcular(total_comparacoes_pior)), round(desvio.media(memoria_pior)),round(desvio.calcular(memoria_pior))])
        #escritor_csv.writerow([tamanho_arranjo, "100 Números Aleatórios", round(desvio.media(tempos_aleatorio)), round(desvio.calcular(tempos_aleatorio)), round(desvio.media(total_comparacoes_aleatorio)), round(desvio.calcular(total_comparacoes_aleatorio)), round(desvio.media(memoria_aleatorio)),round(desvio.calcular(memoria_aleatorio))])

    print("Novos resultados adicionados com sucesso no arquivo:", nome_arquivo_csv)

    # Liberando a memória
    #del desvio, casos_piores, total_comparacoes_pior, tempos_pior, memoria_pior, comparacoes_aleatorio_arranjo, total_comparacoes_aleatorio, tempos_aleatorio, memoria_aleatorio, numeros_aleatorios

print("Testes Finalizados!!")
