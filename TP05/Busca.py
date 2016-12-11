import datetime

def buscaSequencial(vetor, elemento):
    for i in range(len(vetor)):
        if elemento == vetor[i]:
            return vetor[i]
            break

def buscaBinaria(vetor, elemento):
    inicio = 0
    fim = len(vetor)-1
    meio = (inicio + fim)//2
    while inicio <= fim:
        if elemento == vetor[meio]:
            return meio
        elif elemento > vetor[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = (inicio + fim)//2
    return -1

def testeDesempenhoSequencial(razao):
    print("\n\nImpressão de tempo de Busca Sequencial")
    vetor = []
    while razao <= 100000000:
        print("Vetor com %d elementos: " % razao)
        for i in range(razao):
            vetor.append(i)
        inicio = datetime.datetime.now()
        buscaSequencial(vetor, razao)
        fim = datetime.datetime.now()
        print(fim-inicio)
        razao *= 10

def testeDesempenhoBinario(razao):
    vetor = []
    print("\n\nImpressão de tempo de Busca Binária")
    while razao <= 100000000:
        print("Vetor com %d elementos: " % razao)
        for i in range(razao):
            vetor.append(i)
        inicio = datetime.datetime.now()
        buscaBinaria(vetor, razao)
        fim = datetime.datetime.now()
        print(fim-inicio)
        razao *= 10

testeDesempenhoSequencial(10)
testeDesempenhoBinario(10)