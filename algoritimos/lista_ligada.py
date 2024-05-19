class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.ja_ordenada = False


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Adicionando referência ao último nó
        self.comparacoes_totais = 0
        
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
        if sort and self.ja_ordenada == False:
            self.ordenar_lista_ligada()

        indice = 0
        current_node = self.head
        while current_node is not None:
            self.comparacoes_totais +=1
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
        self.ja_ordenada = True

        # Recriar a lista ligada com os valores ordenados
        self.head = None
        self.tail = None
        for value in values:
            self.append(value)