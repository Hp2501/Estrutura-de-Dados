lista = [ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5], [3,8], [4,5], [4,9], [7,8], [7,9] ]

def grafListaParaMatriz(lista):
    m = [[0 for x in range(max(max(lista)) + 1)] for y in range(max(max(lista)) + 1)]
    for i in range(len(lista)):
        b = lista[i]
        m[b[0]][b[1]] = 1
        m[b[1]][b[0]] = 1
    return m

def grafMatrizParaLista(m):
    l = []
    z = -1
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != 0:
                sublista = [i, j]
                l.append(sublista)
    tamLista = len(l)
    while z < tamLista:
        z += 1
        y = 0
        while y < tamLista:
            try:
                if l[z] == l[y][::-1]:
                    l.pop(y)
                    tamLista = len(l)
                else:
                    y += 1
            except IndexError:
                break
    return l

def imprimirMatriz(m):
    for i in range(len(m)):
        print(m[i])