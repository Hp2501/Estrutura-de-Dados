def iniciarVertice(*v):
    vertice = {}
    if len(v) == 0:
        vertice['conteudo'] = []
    else:
        vertice['conteudo'] = v[0]
    vertice['filhos'] = {}
    return vertice

def adcionarConteudo(v, cont):
    v['conteudo'].append(cont)
    return v

def adcionarFilho(vPai, vFilho, ref):
    vPai['filhos'][ref] = vFilho
    return vPai

def verificarVertice(palavra, vertice, indice):
    if palavra[indice] in vertice['filhos']:
        verificarVertice(palavra[indice+1:], vertice['filhos'][indice], indice+1)
        if len(palavra) == 0:
            if len(vertice['conteudo']) != 0:
                return True
            else:
                return False
    else:
        return False


raiz = iniciarVertice()
palavra = input("Digite a palavra: ")
if verificarVertice(palavra, raiz, 0) is False:
    print("\nA palavra não existe no dicionário. Gostaria de adcionar a palavra? ")
    print("1 - Sim")
    print("2 - Não")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        vPai = raiz
        for i in range(len(palavra)):
            adcionarFilho(vPai, iniciarVertice(), palavra[i])
            vPai = vPai['filhos'][palavra[i]]
        definicao = input("Digite a definição: ")
        adcionarConteudo(vPai, definicao)