import random

range_dos_numeros = 1_000_000

arranjo_100k = random.sample(range(0, range_dos_numeros), 100_000)
print(arranjo_100k)

with open("./arquivos_testes/arranjo_100_mil.txt", "w") as f:
    for number in arranjo_100k:
        f.write(str(number) + "\n")