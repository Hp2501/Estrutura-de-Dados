class Pessoa:
    def __init__(self, n, i, c):
        self.nome = n
        self.idade = i
        self.cpf = c

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, n):
        if not n:
            raise Exception("CAMPO NOME VAZIO")
        else:
            self._nome = n

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, i):
        if i < 0:
            self._idade = 0
        else:
            self._idade = i

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, c):
        if len(c) < 11:
            self._cpf = '11111111111'
        else:
            self._cpf = c