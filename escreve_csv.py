import csv
import random
import os
from lista_ligada import LinkedList
from medidores import medir_tempo, memoria_processo, get_pid, DesvioPadrao


def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, "r") as arquivo_aberto:
        for number in arquivo_aberto:
            lista.append(number.strip())
    return lista

pid = get_pid()
nome_arquivo = './arranjo_1_milhao.txt'

lista = ler_arquivo(nome_arquivo)
tamanho_arranjo = len(lista)

#instanciei
lista_ligada = LinkedList()

lista_ligada.comparacoes_totais = 0

inicio_memoria_pior = memoria_processo()

# Preenche a lista ligada
for x in lista:
    lista_ligada.append(x)

# Ordena Lista Ligada
#lista_ligada.ordenar_lista_ligada()

#ordena vetor chamado lista
#lista.sort(reverse=False)

#Escolhe os piores casos para teste
pior_caso1 = -1
pior_caso2 = -50
pior_caso3 = -90
#pior_caso3 = lista[-1] #funciona se a lista estiver ordenada

'--------- Pio Cenário ---------'
inicio_tempo_pior = medir_tempo()

lista_ligada.busca_sequencial_lista_ligada(valor=pior_caso1)
comparacoes_1 = lista_ligada.comparacoes_totais

lista_ligada.comparacoes_totais = 0
lista_ligada.busca_sequencial_lista_ligada(valor=pior_caso2)
comparacoes_2 = lista_ligada.comparacoes_totais

lista_ligada.comparacoes_totais = 0
lista_ligada.busca_sequencial_lista_ligada(valor=pior_caso3)
comparacoes_3 = lista_ligada.comparacoes_totais

# Usando a classe DesvioPadrao
desvio = DesvioPadrao()
numeros = [comparacoes_1, comparacoes_2, comparacoes_3]
desvio_padrao_resultado = desvio.calcular(numeros)

fim_tempo_pior = medir_tempo()
fim_memoria_pior = memoria_processo()

tempo_pior = (fim_tempo_pior - inicio_tempo_pior) * 1000  # Convertendo para ms
memoria_consumida_pior = fim_memoria_pior - inicio_memoria_pior

# 100 números aleatórios da lista enviada

'--------- 100 Números Aleatórios ---------'

total_de_buscas_aleatorias = 100
numeros_aleatorios = random.sample(lista, total_de_buscas_aleatorias)

inicio_tempo_aleatorio = medir_tempo()
#usar a mesma variavel
inicio_memoria_aleatorio = memoria_processo()

for x in numeros_aleatorios:
    lista_ligada.busca_sequencial_lista_ligada(valor=x)

fim_tempo_aleatorio = medir_tempo()
fim_memoria_aleatorio = memoria_processo()

tempo_aleatorio = (fim_tempo_aleatorio - inicio_tempo_aleatorio) * 1000  # Convertendo para ms
memoria_consumida_aleatorio = fim_memoria_aleatorio - inicio_memoria_aleatorio

# Salva os resultados em um arquivo CSV
nome_arquivo_csv = 'resultados_teste.csv'
# Verifica se o arquivo CSV já existe
arquivo_existe = os.path.isfile(nome_arquivo_csv)

with open(nome_arquivo_csv, mode='a', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escreve cabeçalhos apenas se o arquivo não existir
    if not arquivo_existe:
        escritor_csv.writerow(["Arranjo", "Tipo de Teste", "Tempo (ms)", "Memória Consumida (KB)", "Comparações", "Memória Inicial (KB)", "Memória Final (KB)","Desvio Padrão Comparações"])
    
    # Adiciona os dados dos testes
    escritor_csv.writerow([tamanho_arranjo, "Pior Cenário", tempo_pior, memoria_consumida_pior / 1024, comparacoes_1 + comparacoes_2 + comparacoes_3, inicio_memoria_pior / 1024, fim_memoria_pior / 1024, desvio_padrao_resultado])
    escritor_csv.writerow([tamanho_arranjo, "100 Números Aleatórios", tempo_aleatorio, memoria_consumida_aleatorio / 1024, lista_ligada.comparacoes_totais, inicio_memoria_aleatorio / 1024, fim_memoria_aleatorio / 1024, desvio_padrao_resultado])

print("Novos resultados adicionados com sucesso no arquivo:", nome_arquivo_csv)
