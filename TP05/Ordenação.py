import datetime

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

def ordQuick(v):
    if len(v) <= 1:
        return v

    pivo = v[0]
    iguais = [x for x in v if x == pivo]
    menores = [x for x in v if x < pivo]
    maiores = [x for x in v if x > pivo]
    return ordQuick(menores) + iguais + ordQuick(maiores)

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


def troca(a, i, j):
    a[i], a[j] = a[j], a[i]

def heap(vetor):
    n = 0
    m = 0
    while True:
        for i in [0, 1]:
            m += 1
            if m >= len(vetor):
                return True
            if vetor[m] > vetor[n]:
                return False
        n += 1

def peneirar(vetor, n, max):
    while True:
        maior = n
        c1 = 2*n + 1
        c2 = c1 + 1
        for c in [c1, c2]:
            if c < max and vetor[c] > vetor[maior]:
                maior = c
        if maior == n:
            return
        troca(vetor, n, maior)
        n = maior

def transformarHeap(vetor):
    i = len(vetor) / 2 - 1
    max = len(vetor)
    while i >= 0:
        peneirar(vetor, i, max)
        i -= 1

def heapsort(vetor):
    transformarHeap(vetor)
    j = len(vetor) - 1
    while j > 0:
        troca(vetor, 0, j)
        j -= 1

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

print("Impressão de tempo de Ordenação BubbleSort")

razao = 100
print("Vetor com 100 elementos: ")
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

print("\n\nImpressão de tempo de Ordenação QuickSort")

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