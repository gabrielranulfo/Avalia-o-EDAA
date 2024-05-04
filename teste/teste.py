import random

range_dos_numeros = 100000

arquivo = list(range(1, range_dos_numeros + 1))  # Gera uma lista de números sequenciais

with open("./teste/teste.txt", "w") as f:
    for number in arquivo:
        f.write(str(number) + "\n")
