import time
import psutil
import os


nome_arquivo = 'arranjo_100_mil.txt'
lista0 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista0.append(number.strip())

nome_arquivo = 'arranjo_200_mil.txt'
lista1 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista1.append(number.strip())

nome_arquivo = 'arranjo_300_mil.txt'
lista2 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista2.append(number.strip())

nome_arquivo = 'arranjo_400_mil.txt'
lista3 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista3.append(number.strip())

nome_arquivo = 'arranjo_500_mil.txt'
lista4 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista4.append(number.strip())

nome_arquivo = 'arranjo_600_mil.txt'
lista5 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista5.append(number.strip())

nome_arquivo = 'arranjo_700_mil.txt'
lista6 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista6.append(number.strip())

nome_arquivo = 'arranjo_800_mil.txt'
lista7 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista7.append(number.strip())

nome_arquivo = 'arranjo_900_mil.txt'
lista8 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista8.append(number.strip())

nome_arquivo = 'arranjo_1_milhao.txt'
lista9 = []
with open(nome_arquivo, "r") as arquivo_aberto:
    for number in arquivo_aberto:
        lista9.append(number.strip())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Adicionando referência ao último nó

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node  # Se a lista estiver vazia, o novo nó é tanto a cabeça quanto o último nó
            return
        self.tail.next = new_node
        self.tail = new_node  # Atualiza o último nó para o novo nó

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def busca_sequencial_lista_ligada(self, valor, sort=False):
        if sort:
            self.ordenar_lista_ligada()

        indice = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == valor:
                return indice
            current_node = current_node.next
            indice += 1
        return -1

    def ordenar_lista_ligada(self):
        values = []
        current_node = self.head
        while current_node is not None:
            values.append(current_node.data)
            current_node = current_node.next
        values.sort()

        # Recriar a lista ligada com os valores ordenados
        self.head = None
        self.tail = None
        for value in values:
            self.append(value)



# Exemplo de uso
#if __name__ == "__main__":
    lista_ligada = LinkedList()
    lista_ligada.append(1)
    lista_ligada.append(2)
    lista_ligada.append(3)
    lista_ligada.append(4)
    lista_ligada.print_list()  # Saída: 1 2 3 4
    print("Busca sequencial:", lista_ligada.busca_sequencial(3))  # Saída: 2
    print("Busca binária:", lista_ligada.busca_binaria(3))  # Saída: 2



def memoria_processo():
    processo = psutil.Process(os.getpid())
    memoria_utilizada = processo.memory_info().rss
    return memoria_utilizada

