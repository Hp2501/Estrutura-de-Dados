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

def verificarVertice(palavra, vertice, indice):
    listaPalavra = list(palavra)
    if len(palavra) == 0 and vertice['conteudo'] is not None:
        return True
    else:
        if palavra[0:1] in vertice['filhos']:
            ref = palavra[0]
            listaPalavra.pop(0)
            palavra = "".join(listaPalavra)
            return verificarVertice(palavra, vertice['filhos'][ref], indice + 1)
        else:
            return False

def verticeFilho(palavra, vertice, indice):
    listaPalavra = list(palavra)
    if len(palavra) == 0:
        return True
    else:
        if palavra[0:1] in vertice['filhos']:
            ref = palavra[0]
            listaPalavra.pop(0)
            palavra = "".join(listaPalavra)
            return verticeFilho(palavra, vertice['filhos'][ref], indice + 1)
        else:
            return vertice

def voltaVertice(palavra, vertice, indice):
    listaPalavra = list(palavra)
    if len(palavra) == 0:
        return vertice
    else:
        if palavra[0:1] in vertice['filhos']:
            ref = palavra[0]
            listaPalavra.pop(0)
            palavra = "".join(listaPalavra)
            return voltaVertice(palavra, vertice['filhos'][ref], indice + 1)
        else:
            return vertice

def fatiaVertice(palavra, vertice, indice):
    listaPalavra = list(palavra)
    if len(palavra) == 0 and vertice['conteudo'] is not None:
        return True
    else:
        if palavra[0:1] in vertice['filhos']:
            ref = palavra[0]
            listaPalavra.pop(0)
            palavra = "".join(listaPalavra)
            return fatiaVertice(palavra, vertice['filhos'][ref], indice + 1)
        else:
            return palavra

def imprimirDefinicao(palavra, vertice, indice):
    listaPalavra = list(palavra)
    if len(palavra) == 0 and vertice['conteudo'] is not None:
        return vertice['conteudo']
    else:
        if palavra[0:1] in vertice['filhos']:
            ref = palavra[0]
            listaPalavra.pop(0)
            palavra = "".join(listaPalavra)
            return imprimirDefinicao(palavra, vertice['filhos'][ref], indice + 1)
        else:
            return False

raiz = iniciarVertice()
vertice = raiz
while (True):
    palavra = input("Digite a palavra: ")
    if not verificarVertice(palavra, raiz, 0):
        print("\nA palavra não existe no dicionário. Gostaria de adcionar a palavra? ")
        print("1 - Sim")
        print("2 - Não")
        print("0 - Sair")
        opcao = int(input("\nEscolha: "))
        if opcao == 1:
            parcial = fatiaVertice(palavra, raiz, 0)
            for i in range(len(parcial)):
                vertice = voltaVertice(palavra, raiz, 0)
                adcionarFilho(verticeFilho(palavra, vertice, 0), iniciarVertice(), fatiaVertice(palavra, raiz, 0)[0])
            definicao = input("Digite a definição: ")
            vertice = voltaVertice(palavra, raiz, 0)
            adcionarConteudo(vertice, definicao)
        elif opcao == 2:
            continue
        elif opcao == 0:
            break
    else:
        significado = imprimirDefinicao(palavra, raiz, 0)
        print("A palavra já existe no dicinário e sua definição é: %s" % significado)