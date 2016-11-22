def bolha(v):
    ultimo = len(v)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        i = 0
        while i < ultimo:
            if v[i] > v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
                ordenado = False
                ultimo = i
            i = i+1
        print("Vetor: %s" %v)

def insercao(v):
    tamVetor = len(v)
    for i in range(1, tamVetor):
        elemAtual = v[i]
        j = i-1
        while j >= 0 and v[j] > elemAtual:
            v[j+1] = v[j]
            j = j-1
        v[j+1] = elemAtual
        print(v)

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