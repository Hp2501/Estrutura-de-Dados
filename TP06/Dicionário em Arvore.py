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
file = open('dicionario.txt', 'r')
listaFile = file.readlines()
listaPalavras = []
listaDefinicao = []
file.close()
i = 0
while i < len(listaFile):
    listaPalavras.append(listaFile[i])
    i += 2

j = 1
while j < len(listaFile):
    listaDefinicao.append(listaFile[j])
    j += 2

for i in range(len(listaPalavras)):
    palavra = listaPalavras[i]
    if not verificarVertice(palavra.lower(), raiz, 0):
        parcial = fatiaVertice(palavra.lower(), raiz, 0)
        for i in range(len(parcial)):
            vertice = voltaVertice(palavra.lower(), raiz, 0)
            adcionarFilho(verticeFilho(palavra.lower(), vertice, 0), iniciarVertice(), fatiaVertice(palavra.lower(), raiz, 0)[0])
for i in raiz(len(listaDefinicao)):
    definicao = listaDefinicao[i]
    vertice = voltaVertice(palavra.lower(), raiz, 0)
    adcionarConteudo(vertice, definicao)


while (True):
    palavra = input("Digite a palavra: ")
    if not verificarVertice(palavra.lower(), raiz, 0):
        print("\nA palavra não existe no dicionário. Gostaria de adcionar a palavra? ")
        print("1 - Sim")
        print("2 - Não")
        print("0 - Sair")
        opcao = int(input("\nEscolha: "))
        if opcao == 1:
            file = open('dicionario.txt', 'a')
            file.write(palavra + '\n')
            file.close()
            parcial = fatiaVertice(palavra.lower(), raiz, 0)
            for i in range(len(parcial)):
                vertice = voltaVertice(palavra.lower(), raiz, 0)
                adcionarFilho(verticeFilho(palavra.lower(), vertice, 0), iniciarVertice(), fatiaVertice(palavra.lower(), raiz, 0)[0])
            definicao = input("Digite a definição: ")
            file = open('dicionario.txt', 'a')
            file.write(definicao + '\n')
            file.close()
            vertice = voltaVertice(palavra.lower(), raiz, 0)
            adcionarConteudo(vertice, definicao)
        elif opcao == 2:
            continue
        elif opcao == 0:
            break
    else:
        significado = imprimirDefinicao(palavra.lower(), raiz, 0)
        print("A palavra já existe no dicinário e sua definição é: %s" % significado)