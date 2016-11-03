from business.Fila import *
from business.Pessoa import Pessoa

print("||FILA CIRCULAR COM ORIENTAÇÃO A OBJETOS||")
fc = iniciarFilaCircular(int(input("Digite a capacidade da fila: ")))

opcao = 0
objeto = []
while opcao != 'sair':
    print("O que gostaria de fazer?")
    print("1 - ADCIONAR PESSOA A FILA")
    print("2 - EXCLUIR PESSOA DA FILA")
    print("3 - IMPRIMIR LISTA")
    opcao = input("Digite o número da opção: ")
    if opcao == '1':
        if estaCheia(fc):
            print("Fila cheia. Exclua algum elemento")
        else:
            n = input("Digite o nome da pessoa: ")
            i = int(input("Digite a idade: "))
            c = input("Digite o CPF: ")
            a = Pessoa(n, i, c)
            entrarFila(fc, a)

    elif opcao == '2':
        if estaVazia(fc):
            print("Fila vazia, não há o que excluir")
        else:
            sairFila(fc)


    elif opcao == '3':
        imprimirFila(fc)