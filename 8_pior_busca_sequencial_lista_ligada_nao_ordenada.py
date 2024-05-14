import csv
import random
import os
from algoritimos.lista_ligada import LinkedList
from medidores.medidores import medir_tempo, get_pid, DesvioPadrao,memoria_fim,memoria_inicio,memoria_total_consumida,esperar

def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, "r") as arquivo_aberto:
        for number in arquivo_aberto:
            lista.append(number.strip())
    return lista

diretorio = './arquivos/'
arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    caminho_arquivo = os.path.join(diretorio, arquivo)

    pid = get_pid()

    lista = ler_arquivo(caminho_arquivo)
    tamanho_arranjo = len(lista)

    #instanciei
    lista_ligada = LinkedList()

    lista_ligada.comparacoes_totais = 0

    inicio_lista = medir_tempo()
    inicio_memoria_lista = memoria_inicio()

    # Preenche
    for x in lista:
        lista_ligada.append(x)

    fim_lista = medir_tempo()
    fim_memoria_lista = memoria_fim()

    print(f"Arranjo {arquivo} Tempo : {(fim_lista - inicio_lista)  * 1e6} (μs) Memória : {memoria_total_consumida(inicio=inicio_memoria_lista,fim=fim_memoria_lista)}")
    #ordena vetor chamado lista
    #lista.sort(reverse=False)

    '--------- Pior Cenário ---------'
    desvio = DesvioPadrao()

    #casos_piores = [-1,-50,lista[-1]] #funciona só se a lista for ordenada
    casos_piores = [-1,-50,-90]
    total_comparacoes_pior = []
    tempos_pior = []
    memoria_pior = []

    for x in casos_piores:
        inicio_tempo_pior = medir_tempo()
        inicio_memoria_pior = memoria_inicio()

        lista_ligada.busca_sequencial_lista_ligada(valor=x,sort=False)
        total_comparacoes_pior.append(lista_ligada.comparacoes_totais)

        fim_tempo_pior = medir_tempo()
        fim_memoria_pior = memoria_fim()

        memoria_pior.append(memoria_total_consumida(inicio=inicio_memoria_pior,fim=fim_memoria_pior))
        tempos_pior.append((fim_tempo_pior - inicio_tempo_pior) * 1e6)

        lista_ligada.comparacoes_totais = 0
        inicio_tempo_pior = 0
        inicio_memoria_pior = 0
        esperar(segundos=1)
        del inicio_tempo_pior,inicio_memoria_pior,fim_tempo_pior,fim_memoria_pior

    desvio_padrao_resultado_pior = desvio.calcular(total_comparacoes_pior)
    media_comparacoes_pior = desvio.media(total_comparacoes_pior)

    tempo_pior = sum(tempos_pior)
    memoria_consumida_pior = sum(memoria_pior)


    # Salva os resultados em um arquivo CSV
    nome_diretorio = './resultados/'
    if not os.path.exists(nome_diretorio):
        os.makedirs(nome_diretorio)

    nome_arquivo_csv = os.path.join(nome_diretorio, 'lista_ligada_nao_ordenada.csv')

    #nome_arquivo_csv = '/resultados/lista_ligada_nao_ordenada.csv'
    # Verifica se o arquivo CSV já existe
    arquivo_existe = os.path.isfile(nome_arquivo_csv)

    with open(nome_arquivo_csv, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Escreve cabeçalhos apenas se o arquivo não existir
        if not arquivo_existe:
            escritor_csv.writerow(["Arranjo", "Tipo de Teste", "Média Tempo (μs)", "Desvio Pradrão Tempo (μs)", "Média Comparações","Desvio Padrão Comparações", "Média Memória (bytes)", "Desvio Padrão Memória (bytes)"])

        # Adiciona os dados dos testes
        escritor_csv.writerow([tamanho_arranjo, "Pior Cenário", round(desvio.media(tempos_pior)), round(desvio.calcular(tempos_pior)), round(desvio.media(total_comparacoes_pior)), round(desvio.calcular(total_comparacoes_pior)), round(desvio.media(memoria_pior)),round(desvio.calcular(memoria_pior))])
        #escritor_csv.writerow([tamanho_arranjo, "100 Números Aleatórios", round(desvio.media(tempos_aleatorio)), round(desvio.calcular(tempos_aleatorio)), round(desvio.media(total_comparacoes_aleatorio)), round(desvio.calcular(total_comparacoes_aleatorio)), round(desvio.media(memoria_aleatorio)),round(desvio.calcular(memoria_aleatorio))])

    print("Novos resultados adicionados com sucesso no arquivo:", nome_arquivo_csv)

    #del memoria_consumida_aleatorio,memoria_consumida_pior,fim_memoria_aleatorio,fim_memoria_pior,inicio_memoria_aleatorio,inicio_memoria_pior
    #del desvio, casos_piores, total_comparacoes_pior, tempos_pior, memoria_pior, comparacoes_aleatorio_lista, total_comparacoes_aleatorio, tempos_aleatorio, memoria_aleatorio, numeros_aleatorios


print("Testes Finalizados!!")