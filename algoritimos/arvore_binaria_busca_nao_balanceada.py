class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
class ArvoreBinariaBuscaNaoBalanceada:
    def __init__(self):
        self.raiz = None
        self.comparacoes_totais = 0
        self.lista_esquerda = []
        self.lista_direita = []
        #self.busca_recursiva = True

    def inserir(self, valor, insercao_recursiva=True):
        '''
        True - Recursiva
        False - Iterativa
        '''
        if insercao_recursiva:
            if self.raiz is None:
                self.raiz = No(valor)
            else:
                self._inserir_recursivamente(self.raiz, valor)
        else:
            self.inserir_iterativo(valor)


    def _inserir_recursivamente(self, no_atual, valor):
        self.comparacoes_totais += 1  # Incrementando o número de comparações
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

    def inserir_iterativo(self, valor):
        novo_no = No(valor)
        if self.raiz is None:
            self.raiz = novo_no
            return
        no_atual = self.raiz
        while True:
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = novo_no
                    return
                else:
                    no_atual = no_atual.esquerda
            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = novo_no
                    return
                else:
                    no_atual = no_atual.direita
            else:
                # Se o valor já existe na árvore, não faz nada
                return

    def buscar(self, valor, busca_recursiva=True):
        '''
        True - Recursiva
        False - Iterativa
        '''
        if busca_recursiva:
            return self._buscar_recursivamente(self.raiz, valor)
        else:
            return self.busca_iterativa(valor)

    def _buscar_recursivamente(self, no_atual, valor):
        if no_atual is None or no_atual.valor == valor:
            return no_atual
        self.comparacoes_totais += 1  # Incrementando o número de comparações
        if valor < no_atual.valor:
            return self._buscar_recursivamente(no_atual.esquerda, valor)
        return self._buscar_recursivamente(no_atual.direita, valor)
    
    def busca_iterativa(self, valor):
        no_atual = self.raiz
        while no_atual is not None and no_atual.valor != valor:
            self.comparacoes_totais += 1
            if valor < no_atual.valor:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita
        return no_atual

    def em_ordem(self):
        elementos = []
        self._em_ordem_recursivamente(self.raiz, elementos)
        return elementos

    def _em_ordem_recursivamente(self, no_atual, elementos):
        if no_atual:
            self._em_ordem_recursivamente(no_atual.esquerda, elementos)
            elementos.append(no_atual.valor)
            self._em_ordem_recursivamente(no_atual.direita, elementos)

    def ver_lados(self):
        raiz = self.raiz.valor if self.raiz else None
        esquerda = []
        direita = []
        
        if self.raiz:
            if self.raiz.esquerda:
                self._adicionar_nos(self.raiz.esquerda, esquerda)
            if self.raiz.direita:
                self._adicionar_nos(self.raiz.direita, direita)
        
        return raiz, esquerda, direita

    def _adicionar_nos(self, no_atual, lista):
        if no_atual:
            lista.append(no_atual.valor)
            self._adicionar_nos(no_atual.esquerda, lista)
            self._adicionar_nos(no_atual.direita, lista)