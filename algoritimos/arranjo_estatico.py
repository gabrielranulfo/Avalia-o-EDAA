class ArranjoEstatico:
    def __init__(self, tamanho):
        self.arranjo = [None] * tamanho
        self.tamanho = tamanho
        self.comparacoes_totais = 0  # Adicionando atributo para contar comparações

    def inserir(self, valor, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            print("Posição inválida!")
            return
        self.arranjo[posicao] = valor

    def buscar_sequencial(self, valor):
        self.comparacoes_totais = 0  # Zerando o contador de comparações
        for i in range(self.tamanho):
            self.comparacoes_totais += 1  # Incrementando o contador
            if self.arranjo[i] == valor:
                return i  # Retorna a posição do valor se encontrado
        return -1  # Retorna -1 se o valor não for encontrado

    def buscar_binaria(self, valor):
        self.comparacoes_totais = 0  # Zerando o contador de comparações
        inicio = 0
        fim = self.tamanho - 1

        while inicio <= fim:
            self.comparacoes_totais += 1  # Incrementando o contador
            meio = (inicio + fim) // 2
            if self.arranjo[meio] == valor:
                return meio  # Retorna a posição do valor se encontrado
            elif self.arranjo[meio] < valor:
                inicio = meio + 1
            else:
                fim = meio - 1

        return -1  # Retorna -1 se o valor não for encontrado
