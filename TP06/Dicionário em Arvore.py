import sys
def iniciarVertice(*v):
    vertice = {}
    if len(v) == 0:
        vertice['conteudo'] = None
    else:
        vertice['conteudo'] = v[0]
    vertice['filhos'] = {}
    return vertice

def adcionarConteudo(v, cont):
    v['conteudo'] = cont
    return v

def adcionarFilho(vPai, vFilho, ref):
    vPai['filhos'][ref] = vFilho
    return vPai

def verificarVertice(vPai, vFilho, ref, item):
    i = 0
    while i > len(item):
        if item[i] in vPai['filhos']:
            vPai = vPai['filhos'][]
        else:
            return False