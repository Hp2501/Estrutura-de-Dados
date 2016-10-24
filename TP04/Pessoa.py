class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.cpf = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        if n != '':
            self.__nome = n
        else:
            raise Exception("Campo nome vazio")

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, id):
        if id > 0:
            self.idade = id
        else:
            raise Exception("Idade inválida")

    @property
    def cpf(self):
        return self.cpf

    @cpf.setter
    def cpf(self, c):
        if len(c) == 11:
            self.cpf = c
        else:
            raise Exception("CPF Inválido")