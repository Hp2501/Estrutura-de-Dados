import datetime

def buscaSequencial(vetor, elemento):
    for i in range(len(vetor)):
        if elemento == vetor[i]:
            return vetor[i]
            break

def buscaBinaria(vetor, elemento):
    inicio = 0
    fim = len(vetor)-1
    meio = (inicio + fim)//2
    while inicio <= fim:
        if elemento == vetor[meio]:
            return meio
        elif elemento > vetor[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = (inicio + fim)//2
    return -1

def testeDesempenhoSequencial(razao):
    vetor = []
    for i in range(razao):
        vetor.append(i)
    inicio = datetime.datetime.now()
    buscaSequencial(vetor, razao-1)
    fim = datetime.datetime.now()
    print(fim - inicio)

def testeDesempenhoBinario(razao):
    vetor = []
    for i in range(razao):
        vetor.append(i)
    inicio = datetime.datetime.now()
    buscaBinaria(vetor, razao-1)
    fim = datetime.datetime.now()
    print(fim - inicio)

razao = 100

testeDesempenhoSequencial(razao)

razao = 1000

testeDesempenhoSequencial(razao)

razao = 10000

testeDesempenhoSequencial(razao)

razao = 100000

testeDesempenhoSequencial(razao)

razao = 1000000

testeDesempenhoSequencial(razao)

razao = 10000000

testeDesempenhoSequencial(razao)

razao = 100000000

testeDesempenhoSequencial(razao)





