import random

range_dos_numeros = 120_000_000

arranjo_100k = random.sample(range(1, range_dos_numeros), 100_000)


with open("arranjo_100_mil.txt", "w") as f:
    for number in arranjo_100k:
        f.write(str(number) + "\n")


arranjo_200k = random.sample(range(1, range_dos_numeros), 200_000)

with open("arranjo_200_mil.txt", "w") as f:
    for number in arranjo_200k:
        f.write(str(number) + "\n")

arranjo_300k = random.sample(range(1, range_dos_numeros), 300_000)

with open("arranjo_300_mil.txt", "w") as f:
    for number in arranjo_300k:
        f.write(str(number) + "\n")


arranjo_400k = random.sample(range(1, range_dos_numeros), 400_000)

with open("arranjo_400_mil.txt", "w") as f:
    for number in arranjo_400k:
        f.write(str(number) + "\n")


arranjo_500k = random.sample(range(1, range_dos_numeros), 500_000)

with open("arranjo_500_mil.txt", "w") as f:
    for number in arranjo_500k:
        f.write(str(number) + "\n")


arranjo_600k = random.sample(range(1, range_dos_numeros), 600_000)

with open("arranjo_600_mil.txt", "w") as f:
    for number in arranjo_600k:
        f.write(str(number) + "\n")


arranjo_700k = random.sample(range(1, range_dos_numeros), 700_000)

with open("arranjo_700_mil.txt", "w") as f:
    for number in arranjo_700k:
        f.write(str(number) + "\n")


arranjo_800k = random.sample(range(1, range_dos_numeros), 800_000)

with open("arranjo_800_mil.txt", "w") as f:
    for number in arranjo_800k:
        f.write(str(number) + "\n")


arranjo_900k = random.sample(range(1, range_dos_numeros), 900_000)

with open("arranjo_900_mil.txt", "w") as f:
    for number in arranjo_900k:
        f.write(str(number) + "\n")


arranjo_1mi = random.sample(range(1, range_dos_numeros), 1_000_000)

with open("arranjo_1_milhao.txt", "w") as f:
    for number in arranjo_1mi:
        f.write(str(number) + "\n")