lista_ligada9 = LinkedList()

inicio_tempo = time.time()
memoria_inicial = memoria_processo()

for x in lista9:
    lista_ligada9.append(x)

memoria_final = memoria_processo()
memoria_consumida = memoria_final - memoria_inicial

fim_tempo = time.time()
tempo = fim_tempo - inicio_tempo

print("-" * 40)
print("Estatisticas da Inserção")
print("-" * 40)
print(f"Tempo : {round(tempo, 9):.4f} seg")
print(f"Memória consumida pelo processo: {memoria_consumida / (1024 ** 3):.4f} GB")
print(f"Memória consumida pelo processo: {memoria_consumida:.4f} bytes")