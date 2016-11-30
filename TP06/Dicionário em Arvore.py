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
    if len(palavra) == 0 and len(vertice['conteudo']) is not None:
        return True
    else:
        if listaPalavra[0] in vertice['filhos']:
            ref = palavra[0]
            listaPalavra.pop(0)
            palavra = "".join(listaPalavra)
            return verificarVertice(palavra, vertice['filhos'][ref], indice + 1)
        else:
            return False

def imprimirDefinicao(palavra, vertice, indice):
    listaPalavra = list(palavra)
    if len(palavra) == 0 and len(vertice['conteudo']) is not None:
        return vertice['conteudo']
    else:
        if listaPalavra[0] in vertice['filhos']:
            ref = palavra[0]
            listaPalavra.pop(0)
            palavra = "".join(listaPalavra)
            return imprimirDefinicao(palavra, vertice['filhos'][ref], indice + 1)
        else:
            return False

raiz = iniciarVertice()
vetor = raiz

while (True):
        palavra = input("Digite a palavra: ")
        if not verificarVertice(palavra, raiz, 0):
            print("\nA palavra não existe no dicionário. Gostaria de adcionar a palavra? ")
            print("1 - Sim")
            print("2 - Não")
            print("0 - Sair")
            opcao = int(input("\nEscolha: "))
            if opcao == 1:
                vetor = raiz
                for i in range(len(palavra)):
                    adcionarFilho(vetor, iniciarVertice(), palavra[i])
                    vetor = vetor['filhos'][palavra[i]]
                definicao = input("Digite a definição: ")
                adcionarConteudo(vetor, definicao)
            elif opcao == 2:
                continue
            elif opcao == 0:
                break
        else:
            significado = imprimirDefinicao(palavra, raiz, 0)
            print("A palavra já existe no dicinário e sua definição é: %s" % significado)