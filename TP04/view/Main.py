from business.Fila import Fila
from business.Pessoa import Pessoa

print("||FILA CIRCULAR COM ORIENTAÇÃO A OBJETOS||")

fc = Fila(int(input("\nDigite a capacidade da fila: ")))

opcao = ''

while opcao.lower() != 'sair':
    print('\nO que gostaria de fazer? DIGITE "SAIR" PARA SAIR')
    print("\n1 - ADCIONAR PESSOA A FILA")
    print("\n2 - EXCLUIR PESSOA DA FILA")
    print("\n3 - IMPRIMIR FILA")

    opcao = input("\nDigite o número da opção: ")

    if opcao == '1':
        if Fila.estaCheia(fc):
            print("\nFila cheia. Exclua algum elemento")
        else:
            n = input("\nDigite o nome da pessoa: ")
            i = int(input("\nDigite a idade: "))
            c = input("\nDigite o CPF: ")
            p = Pessoa(n, i, c)
            a = []
            a.append(p.nome)
            a.append(p.idade)
            a.append(p.cpf)
            Fila.entrarFila(fc, a)

    elif opcao == '2':
        if not Fila.estaVazia(fc):
            Fila.sairFila(fc)
            print(Fila.imprimirFila(fc))
        else:
            print("\nFila vazia, não há o que excluir")

    elif opcao == '3':
        if not Fila.estaVazia(fc):
            print(Fila.imprimirFila(fc))
        else:
            print("\nFila vazia")