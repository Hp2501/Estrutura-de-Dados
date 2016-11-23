import datetime
import sys

sys.setrecursionlimit(150000)

def bolha(v):
    tamVetor = len(v)
    for i in range(1, tamVetor):
        for j in range(0, tamVetor - i):
            if v[j] > v[j+1]:
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux
    return v

def insercao(v):
    tamVetor = len(v)
    for i in range(1, tamVetor):
        elemAtual = v[i]
        j = i-1
        while j >= 0 and v[j] > elemAtual:
            v[j+1] = v[j]
            j = j-1
        v[j+1] = elemAtual
        return v

def intercala(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def ordenacaoMerge(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = ordenacaoMerge(v[:m])
        d = ordenacaoMerge(v[m:])
        return intercala(e, d)

def ordQuick(vetor):
    if len(vetor) > 1:
        pivo = vetor[0]
        maiores = []
        menores = []
        iguais = []
        for e in vetor:
            if e > pivo:
                maiores.append(e)
            elif e < pivo:
                menores.append(e)
            else:
                iguais.append(e)
        return ordQuick(menores) + iguais + ordQuick(maiores)
    else:
        return vetor

def ordSelecao(v):
    for i in range(len(v)):
        posMin = i
        j = i + 1
        while j < len(v):
            if v[posMin] > v[j]:
                posMin = j
            j += 1
        aux = v[i]
        v[i] = v[posMin]
        v[posMin] = aux
    return v


def heapsort(vetor):
    tamanho = len(vetor) - 1
    parente = tamanho // 2
    for i in range(parente, -1, -1):
        mover(vetor, i, tamanho)
    for i in range(tamanho, 0, -1):
        if vetor[0] > vetor[i]:
            troca(vetor, 0, i)
            mover(vetor, 0, i - 1)


def mover(vetor, inicio, fim):
    maior = 2 * inicio + 1
    while maior <= fim:
        if (maior < fim) and (vetor[maior] < vetor[maior + 1]):
            maior += 1
        if vetor[maior] > vetor[inicio]:
            troca(vetor, maior, inicio)
            inicio = maior;
            maior = 2 * inicio + 1
        else:
            return


def troca(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def testeDesempenhoBolha(razao):
    vetor = []
    for i in range(razao):
        vetor.insert(0, i)
    inicio = datetime.datetime.now()
    bolha(vetor)
    fim = datetime.datetime.now()
    print(fim-inicio)

def testeDesempenhoInsercao(razao):
    vetor = []
    for i in range(razao):
        vetor.insert(0, i)
    inicio = datetime.datetime.now()
    insercao(vetor)
    fim = datetime.datetime.now()
    print(fim-inicio)

def testeDesempenhoMerge(razao):
    vetor = []
    for i in range(razao):
        vetor.insert(0, i)
    inicio = datetime.datetime.now()
    ordenacaoMerge(vetor)
    fim = datetime.datetime.now()
    print(fim-inicio)

def testeDesempenhoQuick(razao):
    vetor = []
    for i in range(razao):
        vetor.insert(0, i)
    inicio = datetime.datetime.now()
    ordQuick(vetor)
    fim = datetime.datetime.now()
    print(fim-inicio)

def testeDesempenhoHeapsort(razao):
    vetor = []
    for i in range(razao):
        vetor.insert(0, i)
    inicio = datetime.datetime.now()
    heapsort(vetor)
    fim = datetime.datetime.now()
    print(fim - inicio)

print("Impressão de tempo de Ordenação QuickSort")

razao = 100
print("Vetor com 100 elementos: ")
testeDesempenhoQuick(razao)
razao = 1000
print("Vetor com 1000 elementos: ")
testeDesempenhoQuick(razao)
razao = 10000
print("Vetor com 10000 elementos: ")
testeDesempenhoQuick(razao)
razao = 100000
print("Vetor com 100000 elementos: ")
testeDesempenhoQuick(razao)
razao = 1000000
print("Vetor com 1000000 elementos: ")
testeDesempenhoQuick(razao)

print("\n\nImpressão de tempo de Ordenação HeapSort")

razao = 100
print("Vetor com 100 elementos: ")
testeDesempenhoHeapsort(razao)
razao = 1000
print("Vetor com 1000 elementos: ")
testeDesempenhoHeapsort(razao)
razao = 10000
print("Vetor com 10000 elementos: ")
testeDesempenhoHeapsort(razao)
razao = 100000
print("Vetor com 100000 elementos: ")
testeDesempenhoHeapsort(razao)
razao = 1000000
print("Vetor com 1000000 elementos: ")
testeDesempenhoHeapsort(razao)

print("\n\nImpressão de tempo de Ordenação InsertionSort")

razao = 100
print("Vetor com 100 elementos: ")
testeDesempenhoInsercao(razao)
razao = 1000
print("Vetor com 1000 elementos: ")
testeDesempenhoInsercao(razao)
razao = 10000
print("Vetor com 10000 elementos: ")
testeDesempenhoInsercao(razao)
razao = 100000
print("Vetor com 100000 elementos: ")
testeDesempenhoInsercao(razao)
razao = 1000000
print("Vetor com 1000000 elementos: ")
testeDesempenhoInsercao(razao)

print("\n\nImpressão de tempo de Ordenação BubbleSort")

razao = 100
print("Vetor com 100 elementos: ")
testeDesempenhoBolha(razao)
razao = 1000
print("Vetor com 1000 elementos: ")
testeDesempenhoBolha(razao)
razao = 10000
print("Vetor com 10000 elementos: ")
testeDesempenhoBolha(razao)
razao = 100000
print("Vetor com 100000 elementos: ")
testeDesempenhoBolha(razao)
razao = 1000000
print("Vetor com 1000000 elementos: ")
testeDesempenhoBolha(razao)

print("\n\nImpressão de tempo de Ordenação MergeSort")

razao = 100
print("Vetor com 100 elementos: ")
testeDesempenhoMerge(razao)
razao = 1000
print("Vetor com 1000 elementos: ")
testeDesempenhoMerge(razao)
razao = 10000
print("Vetor com 10000 elementos: ")
testeDesempenhoMerge(razao)
razao = 100000
print("Vetor com 100000 elementos: ")
testeDesempenhoMerge(razao)
razao = 1000000
print("Vetor com 1000000 elementos: ")
testeDesempenhoMerge(razao)