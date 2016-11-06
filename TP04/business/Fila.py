class Fila:
    def __init__(self, cap):
        self.dados = []
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0
        if cap < 5:
            print("Limite minimo para fila é 5. A fila será configurada para 5.")
            self.capacidade = 5
        else:
            self.capacidade = cap

    def estaVazia(self):
        if len(self.dados) == 0:
            return True
        else:
            return False

    def estaCheia(self):
        if len(self.dados) == self.capacidade:
            return True
        else:
            return False

    def entrarFila(self, e):
        if not self.estaCheia():
            self.dados.append(e)
        else:
            print("Fila Cheia")

    def sairFila(self):
        if not self.estaVazia():
            return self.dados.pop(0)
        else:
            print("Fila Vazia")

    def imprimirFila(self):
        return self.dados