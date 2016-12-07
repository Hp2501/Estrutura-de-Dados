def buscaBoyerMoore(texto, padrao):
    ocorrencias = []
    tamanho = len(padrao)
    fim = len(padrao) - 1
    i = j = fim
    while i < len(texto):
        if texto[i] == padrao[j]:
            k = i
            while j > 0:
                i -= 1
                j -= 1
                if texto[i] != padrao[j]:
                    i = k + fim
                    j = fim
                    break
            if j == 0:
                ocorrencias.append(i)
                i = k + fim
                j = fim
        else:
            try:
                mpos = padrao.rindex(texto[i])
                shift = fim - mpos
                i += shift
                continue
            except ValueError:
                i += tamanho
                continue
    return ocorrencias

def trocaBoyerMoore(texto, padrao, sub, ocorrencias):
    listaTexto = list(texto)
    i = 0
    stringModificada = []
    while i < len(texto):
        if i != ocorrencias[0]:
            stringModificada.append(listaTexto[i])
            i += 1
        else:
            stringModificada.append(sub)
            i += len(padrao)
            ocorrencias.pop(0)
            if len(ocorrencias) == 1:
                ocorrencias.append(len(texto)+1)
    stringFinal = "".join(stringModificada)
    return stringFinal

opcao = ''
while opcao != 0:
    print("A entrada será manual ou automática?")
    print("1 - Manual")
    print("2 - Automática")
    print("0 - Sair")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        texto = input("Entre com o texto: ")
        padrao = input("Qual será o padrão a ser buscado: ")
        ocorrencias = buscaBoyerMoore(texto, padrao)
        print("O padrão foi encontrado nos seguintes indices: ", ocorrencias)
        print("\nGostaria de modificar o texto? ")
        print("1 - Sim")
        print("2 - Não")
        opcao2 = int(input("Escolha: "))
        if opcao2 == 1:
            sub = input("\nQual o texto que você gostaria de colocar no lugar do padrão: ")
            textoNovo = trocaBoyerMoore(texto, padrao, sub, ocorrencias)
            print(textoNovo)
        elif opcao2 == 2:
            continue

    elif opcao == 2:
        nomeArquivo = input("Qual o nome do arquivo: ")
        file = open(nomeArquivo, 'r+')
        texto = file.read()
        file.close()
        padrao = input("Qual será o padrao a ser procurado: ")
        ocorrencias = buscaBoyerMoore(texto, padrao)
        print("O padrão foi encontrado nos seguintes indices: ", ocorrencias)
        print("\nGostaria de modificar o texto? ")
        print("1 - Sim")
        print("2 - Não")
        opcao2 = int(input("Escolha: "))
        if opcao2 == 1:
            sub = input("\nQual o texto que você gostaria de colocar no lugar do padrão: ")
            file = open(nomeArquivo, 'a')
            textoNovo = trocaBoyerMoore(texto, padrao, sub, ocorrencias)
            file.write(textoNovo)
            file.close()
        elif opcao2 == 2:
            continue
    elif opcao == 0:
        break