class MinhaClasse:
    def __init__(self, valor):
        self.atributo = valor

    @property
    def atributo(self):
        return self._atributo

    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor

obj = MinhaClasse(1)
print(obj.atributo)
obj.atributo = 2
print(obj.atributo)