matriz_entrada = [
[0,0,1,1,0,0,1,0,1,0],
[0,1,1,0,0,0,1,0,1,0],
[0,0,1,1,0,0,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0,1,0],
[0,0,1,0,0,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0],
[0,0,1,0,0,0,1,1,1,0],
[0,0,1,0,0,0,1,1,1,0]
]


def ler_matriz(matriz: list) -> list:
    """Função que varre a matriz"""
    vistos = []
    x = 1
    linhas = len(matriz)
    colunas = len(matriz[0])
    matriz_saida = matriz
    for linha in range(linhas):
        for coluna in range(colunas):
            posicao = "[%d][%d]" % (linha, coluna)
            if posicao not in vistos and matriz[linha][coluna] != 0:
                matriz_saida, vistos = ler_parentes(matriz, matriz_saida, linha, coluna, x, posicao, vistos)
                x += 1

    return matriz_saida


def ler_parentes(matriz, matriz_saida, linha, coluna, x, posicao, vistos):
    """Verifica a posição atual de uma matriz e seus adjacentes em busca de ocorrencias

    Retorna as posições de ocorrencias e uma matrix modificada"""
    try:
        if matriz[linha][coluna] != 0:
            if posicao not in vistos:
                matriz_saida[linha][coluna] = x
                vistos.append(posicao)
            try:
                if matriz[linha][coluna - 1] != 0:
                    posicao = "[%d][%d]" % (linha, coluna-1)
                    if posicao not in vistos:
                        ler_parentes(matriz, matriz_saida, linha, coluna - 1, x, posicao, vistos)
                        vistos.append(posicao)
            except IndexError:
                pass
            try:
                if matriz[linha - 1][coluna] != 0:
                    posicao = "[%d][%d]" % (linha - 1, coluna)
                    if posicao not in vistos:
                        ler_parentes(matriz, matriz_saida, linha - 1, coluna, x, posicao, vistos)
                        vistos.append(posicao)
            except IndexError:
                pass
            try:
                if matriz[linha][coluna + 1] != 0:
                    posicao = "[%d][%d]" % (linha, coluna + 1)
                    if posicao not in vistos:
                        ler_parentes(matriz, matriz_saida, linha, coluna + 1, x, posicao, vistos)
                        vistos.append(posicao)
            except IndexError:
                pass
            try:
                if matriz[linha + 1][coluna] != 0:
                    posicao = "[%d][%d]" % (linha + 1, coluna)
                    if posicao not in vistos:
                        ler_parentes(matriz, matriz_saida, linha + 1, coluna, x, posicao, vistos)
                        vistos.append(posicao)
            except IndexError:
                pass
    except IndexError:
        pass
    return matriz_saida, vistos



def imprimir_matriz(matriz: list):
    """Imprime uma matriz"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    for linha in range(linhas):
        # Lê a linha
        for coluna in range(colunas):
            print(matriz[linha][coluna], end="")
        print()

def main():
    """Execução principal"""
    print("======Matriz de Entrada======")
    imprimir_matriz(matriz_entrada)
    print("=============================")
    print()
    print("=======Matriz de Saída=======")
    imprimir_matriz(ler_matriz(matriz_entrada))
    print("=============================")
    
if __name__ == "__main__":
    main()

