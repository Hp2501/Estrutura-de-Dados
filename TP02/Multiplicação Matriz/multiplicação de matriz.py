import random

def criarMatriz(linha, coluna):
    a = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            linha = linha + [float(input("Posição [%d][%d]: " %(i+1, j+1)))]
        a = a + [linha]
    return a

def matrizVazia(linha, coluna):
    a = []
    for i in range(linha):
        b = []
        for j in range(coluna):
            b += [random.randint(1,10)]
        a += b
    return a

def imprimirMatriz(linha, coluna, matriz):
    print("Matriz")
    for i in range(linha):
        for j in range(coluna):
            print("%f" %(matriz[i][j]))

def multMatriz(linha, coluna, matA, matB):
    tamanhoL = len(matA)
    tamanhoC = len(matB[0])
    c = [[0 for lin in range(len(matA))] for col in range(len(matB[0]))]
    for i in range(linha):
        for j in range(coluna):
            soma = 0
            for k in range(linha):
                c[i][j] += matA[i][k] * matB[k][j]
    return c

linha1 = int(input("Digite o número de linhas da primeira matriz: "))
coluna1 = int(input("Digite o número de colunas da primeira matriz: "))
matA = criarMatriz(linha1, coluna1)
imprimirMatriz(linha1, coluna1, matA)

linha2 = int(input("Digite o número de linhas da segunda matriz: "))
coluna2 = int(input("Digite o número de colunas da segunda matriz: "))
matB = criarMatriz(linha2, coluna2)
imprimirMatriz(linha2, coluna2, matB)

matC = multMatriz(linha2, coluna1, matA, matB)
imprimirMatriz(linha2, coluna1, matC)
