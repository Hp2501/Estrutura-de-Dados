def iniciarFilaCircular(cap):
    inicio = 0
    fim = 0
    tamanho = 0
    if cap < 5:
        print("Capacidade inferior a permitida, irei criar uma fila de capacidade 5")
        capacidade = 5
    else:
        capacidade = cap
    conteudo = [None]*cap
    filaCircular = {'conteudo':conteudo, 'inicio':inicio, 'fim':fim, 'capacidade':capacidade, 'tamanho':tamanho}
    return filaCircular

def estaVazia(fc):
    if fc['tamanho'] == 0:
        return True
    else:
        return False

def estaCheia(fc):
    if fc['tamanho'] == fc['capacidade']:
        return True
    else:
        return False

def entrarFila(fc, e):
    if estaCheia(fc):
        print("Erro! Fila Cheia!")
    else:
        fc['conteudo'][fc['fim']] = e
        fc['fim'] = (fc['fim' + 1]) % fc['capacidade']
        fc['tamanho'] = fc['tamanho'] + 1

def sairFila(fc):
    if estaVazia(fc):
        print("Erro! Fila Vazia!")
        return -1
    else:
        e = fc['conteudo'][fc['inicio']]
        fc['inicio'] = (fc['inicio' + 1]) % fc['capacidade']
        fc['tamanho'] = fc['tamanho'] - 1