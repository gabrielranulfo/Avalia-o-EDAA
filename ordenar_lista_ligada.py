from ler_arquivo import ler_arquivo
from lista_ligada import Node,LinkedList
from medidores import memoria_total, tempo_total,medir_tempo, memoria_inicio,memoria_fim,memoria_total_consumida,esperar

nome_arquivo100k = 'arranjo_100_mil.txt'
lista100k = ler_arquivo(nome_arquivo100k)
lista_ligada100k = LinkedList()


'------Preencher Lista Ligada------'

for x in lista100k:
    #print(x)
    lista_ligada100k.append(x)


'------Ordenar Lista Ligada------'

inicio_tempo = medir_tempo()
inicio_memoria = memoria_inicio()

lista_ligada100k.ordenar_lista_ligada()

fim_tempo = medir_tempo()
fim_memoria = memoria_fim()


memoria_consumida = memoria_total_consumida(inicio_memoria,fim_memoria)
tempo = tempo_total(inicio=inicio_tempo,fim=fim_tempo)

print("-" * 40)
print("Estatisticas da Ordenação")
print("-" * 40)
print(f"Tempo : {round(tempo, 9):.4f} seg")
print(f"Memória consumida pelo processo: {memoria_consumida} bytes")