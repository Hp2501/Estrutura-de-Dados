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
    vetor = []
    for i in range(razao):
        vetor.append(i)
    inicio = datetime.datetime.now()
    buscaSequencial(vetor, razao-1)
    fim = datetime.datetime.now()
    print(fim-inicio)

def testeDesempenhoBinario(razao):
    vetor = []
    for i in range(razao):
        vetor.append(i)
    inicio = datetime.datetime.now()
    buscaBinaria(vetor, razao-1)
    fim = datetime.datetime.now()
    print(fim-inicio)

print("Impressão de tempo de Busca Sequencial")
razao = 100
print("Vetor com 100 elementos")
testeDesempenhoSequencial(razao)
razao = 1000
print("Vetor com 1000 elementos")
testeDesempenhoSequencial(razao)
razao = 10000
print("Vetor com 10000 elementos")
testeDesempenhoSequencial(razao)
razao = 100000
print("Vetor com 100000 elementos")
testeDesempenhoSequencial(razao)
razao = 1000000
print("Vetor com 1000000 elementos")
testeDesempenhoSequencial(razao)
razao = 10000000
print("Vetor com 10000000 elementos")
testeDesempenhoSequencial(razao)
razao = 100000000
print("Vetor com 100000000 elementos")
testeDesempenhoSequencial(razao)

print("\nImpressão de tempo de Busca Binária")
razao = 100
print("Vetor com 100 elementos")
testeDesempenhoBinario(razao)
razao = 1000
print("Vetor com 1000 elementos")
testeDesempenhoBinario(razao)
razao = 10000
print("Vetor com 10000 elementos")
testeDesempenhoBinario(razao)
razao = 100000
print("Vetor com 100000 elementos")
testeDesempenhoBinario(razao)
razao = 1000000
print("Vetor com 1000000 elementos")
testeDesempenhoBinario(razao)
razao = 10000000
print("Vetor com 10000000 elementos")
testeDesempenhoBinario(razao)
razao = 100000000
print("Vetor com 100000000 elementos")
testeDesempenhoBinario(razao)