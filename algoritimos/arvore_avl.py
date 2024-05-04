class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1  # Altura da árvore começando em 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.comparacoes_totais = 0
        self.fator_balanceamento_atualizado = {}

    def inserir(self, valor):
        self.raiz = self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no_atual, valor):
        # Passo 1: Inserção normal de uma árvore binária de busca
        if not no_atual:
            return No(valor)
        elif valor < no_atual.valor:
            no_atual.esquerda = self._inserir_recursivamente(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._inserir_recursivamente(no_atual.direita, valor)

        # Passo 2: Atualizar a altura do nó ancestral
        no_atual.altura = 1 + max(self._obter_altura(no_atual.esquerda), self._obter_altura(no_atual.direita))

        # Passo 3: Obter o fator de balanceamento do nó
        fator_balanceamento = self._obter_fator_balanceamento(no_atual)
        self.fator_balanceamento_atualizado[no_atual.valor] = fator_balanceamento

        # Passo 4: Se o nó estiver desbalanceado, realizar rotações
        # Rotação simples à direita
        if fator_balanceamento > 1 and valor < no_atual.esquerda.valor:
            return self._rotacao_direita(no_atual)

        # Rotação simples à esquerda
        if fator_balanceamento < -1 and valor > no_atual.direita.valor:
            return self._rotacao_esquerda(no_atual)

        # Rotação dupla à direita
        if fator_balanceamento > 1 and valor > no_atual.esquerda.valor:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Rotação dupla à esquerda
        if fator_balanceamento < -1 and valor < no_atual.direita.valor:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def _obter_altura(self, no_atual):
        if not no_atual:
            return 0
        return no_atual.altura

    def _obter_fator_balanceamento(self, no_atual):
        if not no_atual:
            return 0
        return self._obter_altura(no_atual.esquerda) - self._obter_altura(no_atual.direita)

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        # Realizar rotação
        y.direita = z
        z.esquerda = T3

        # Atualizar alturas
        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        # Realizar rotação
        y.esquerda = z
        z.direita = T2

        # Atualizar alturas
        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no_atual, valor):
        
        if not no_atual or no_atual.valor == valor:
            self.comparacoes_totais += 1 
            return no_atual

        if valor < no_atual.valor:
            self.comparacoes_totais += 1 
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
    

    def imprimir_fator_balanceamento(self):
        self._imprimir_fator_balanceamento_recursivamente(self.raiz)

    def _imprimir_fator_balanceamento_recursivamente(self, no_atual):
        if no_atual is not None:
            self._imprimir_fator_balanceamento_recursivamente(no_atual.esquerda)
            print(f"Valor: {no_atual.valor}, Fator de balanceamento: {self.fator_balanceamento_atualizado[no_atual.valor]}")
            self._imprimir_fator_balanceamento_recursivamente(no_atual.direita)
