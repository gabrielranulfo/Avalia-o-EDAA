import csv
import random
import os
from algoritimos.arvore_binaria_busca_nao_balanceada import ArvoreBinariaBuscaNaoBalanceada
from medidores.medidores import medir_tempo, get_pid, DesvioPadrao, memoria_fim, memoria_inicio, memoria_total_consumida,esperar

def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, "r") as arquivo_aberto:
        for number in arquivo_aberto:
            lista.append(int(number.strip()))  # Convertendo para inteiros
    #lista.sort()
    return lista

diretorio = './arquivos/'
arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    caminho_arquivo = os.path.join(diretorio, arquivo)

    pid = get_pid()

    lista = ler_arquivo(caminho_arquivo)
    tamanho_arranjo = len(lista)

    # Instanciando a árvore binária de busca
    arvore = ArvoreBinariaBuscaNaoBalanceada()

    arvore.comparacoes_totais = 0

    # Preenche a árvore binária de busca
    for x in lista:
        arvore.inserir(x,insercao_recursiva=True)

    raiz, esquerda, direita = arvore.ver_lados()

    print("Raiz:", raiz)
    print("Nós da esquerda:", len(esquerda))
    print("Nós da direita:", len(direita))

    '--------- Pior Cenário ---------'
    desvio = DesvioPadrao()

    casos_piores = [-1, -50, -90]
    total_comparacoes_pior = []
    tempos_pior = []
    memoria_pior = []

    for x in casos_piores:
        inicio_tempo_pior = medir_tempo()
        inicio_memoria_pior = memoria_inicio()

        arvore.buscar(x,busca_recursiva=True)
        total_comparacoes_pior.append(arvore.comparacoes_totais)
        #esperar(0.5)

        fim_tempo_pior = medir_tempo()
        fim_memoria_pior = memoria_fim()

        memoria_pior.append(memoria_total_consumida(inicio=inicio_memoria_pior, fim=fim_memoria_pior))
        #tempos_pior.append((fim_tempo_pior - inicio_tempo_pior) * 1_000_000)
        tempos_pior.append((fim_tempo_pior - inicio_tempo_pior)* 1e6)

        #print(f"Fim : {fim_tempo_pior:.12f} Começo : {inicio_tempo_pior:.12f} Cálculo : {fim_tempo_pior - inicio_tempo_pior:.12f} ")
        #print(f"Fim : {fim_tempo_pior:.2e} Começo : {inicio_tempo_pior:.2e} Cálculo : {fim_tempo_pior - inicio_tempo_pior:.2e} ")

        arvore.comparacoes_totais = 0
    
    
    desvio_padrao_resultado_pior = desvio.calcular(total_comparacoes_pior)
    media_comparacoes_pior = desvio.media(total_comparacoes_pior)

    tempo_pior = sum(tempos_pior)
    memoria_consumida_pior = sum(memoria_pior)

    '--------- 100 Números Aleatórios ---------'

    total_de_buscas_aleatorias = 100
    numeros_aleatorios = random.sample(lista, total_de_buscas_aleatorias)

    total_comparacoes_aleatorio = []
    tempos_aleatorio = []
    memoria_aleatorio = []

    for x in numeros_aleatorios:
        inicio_tempo_aleatorio = medir_tempo()
        inicio_memoria_aleatorio = memoria_inicio()

        arvore.buscar(x,busca_recursiva=True)
        total_comparacoes_aleatorio.append(arvore.comparacoes_totais)

        fim_tempo_aleatorio = medir_tempo()
        fim_memoria_aleatorio = memoria_fim()

        memoria_aleatorio.append(memoria_total_consumida(inicio=inicio_memoria_aleatorio, fim=fim_memoria_aleatorio))
        tempos_aleatorio.append((fim_tempo_aleatorio - inicio_tempo_aleatorio)* 1e6)

        arvore.comparacoes_totais = 0

    desvio_padrao_resultado_aleatorio = desvio.calcular(total_comparacoes_aleatorio)
    media_comparacoes_aleatorio = desvio.media(total_comparacoes_aleatorio)

    tempo_aleatorio = sum(tempos_aleatorio)
    memoria_consumida_aleatorio = sum(memoria_aleatorio)

    # Salva os resultados em um arquivo CSV
    nome_diretorio = './resultados/'
    if not os.path.exists(nome_diretorio):
        os.makedirs(nome_diretorio)

    nome_arquivo_csv = os.path.join(nome_diretorio, 'arvore_binaria_busca_nao_ordenada_nao_balanceada2.csv')

    with open(nome_arquivo_csv, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        if os.stat(nome_arquivo_csv).st_size == 0:
            escritor_csv.writerow(["Arranjo", "Tipo de Teste", "Média Tempo (μs)", "Desvio Pradrão Tempo (μs)", "Média Comparações", "Desvio Padrão Comparações", "Média Memória (bytes)", "Desvio Padrão Memória (bytes)"])

        escritor_csv.writerow([tamanho_arranjo, "Pior Cenário",round(desvio.media(tempos_pior)), round(desvio.calcular(tempos_pior)), round(desvio.media(total_comparacoes_pior)), round(desvio.calcular(total_comparacoes_pior)), round(desvio.media(memoria_pior)), round(desvio.calcular(memoria_pior))])
        escritor_csv.writerow([tamanho_arranjo, "100 Números Aleatórios", round(desvio.media(tempos_aleatorio)), round(desvio.calcular(tempos_aleatorio)), round(desvio.media(total_comparacoes_aleatorio)), round(desvio.calcular(total_comparacoes_aleatorio)), round(desvio.media(memoria_aleatorio)), round(desvio.calcular(memoria_aleatorio))])

    print("Novos resultados adicionados com sucesso no arquivo:", nome_arquivo_csv)

    # Liberando a memória
    del desvio, casos_piores, total_comparacoes_pior, tempos_pior, memoria_pior, total_comparacoes_aleatorio, tempos_aleatorio, memoria_aleatorio, numeros_aleatorios

print("Testes Finalizados!!")