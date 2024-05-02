class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivamente(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivamente(no_atual.direita, valor)
        # Se o valor já existe na árvore, não faz nada

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no_atual, valor):
        if no_atual is None or no_atual.valor == valor:
            return no_atual
        if valor < no_atual.valor:
            return self._buscar_recursivamente(no_atual.esquerda, valor)
        return self._buscar_recursivamente(no_atual.direita, valor)

    def em_ordem(self):
        elementos = []
        self._em_ordem_recursivamente(self.raiz, elementos)
        return elementos

    def _em_ordem_recursivamente(self, no_atual, elementos):
        if no_atual:
            self._em_ordem_recursivamente(no_atual.esquerda, elementos)
            elementos.append(no_atual.valor)
            self._em_ordem_recursivamente(no_atual.direita, elementos)

# Exemplo de uso:
arvore = ArvoreBinariaBusca()
valores = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for valor in valores:
    arvore.inserir(valor)

print("Elementos em ordem crescente:", arvore.em_ordem())
print("Buscando o valor 6:", arvore.buscar(6))
