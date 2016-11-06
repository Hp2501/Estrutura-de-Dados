def numeros(s, sep):  # recebe como parametro uma String e os separadores
    pilha = [s]  # inicia uma pilha com a String passada
    for i in sep:  # varre a string e remove cada separador encontrado
        pedaco = []
        for j in pilha:
            pedaco.extend(j.split(i))
        pilha = pedaco
    return pilha  # retorna a pilha agora sem separador


def operadores(s):  # recebe como parametro uma String
    semNumero = []  # inicia uma lista vazia
    for i in s:  # varre a lista atras de digito, caso não seja digito é adcionado a lista
        if not i.isdigit():
            semNumero.append(i)
    return semNumero  # retorna lista


def converterString(pilhaNumeros):  # recebe uma lista de string
    a = []  # inicia uma lista vazia
    while pilhaNumeros[0] == '':
        pilhaNumeros.pop(0)
    for i in range(len(pilhaNumeros)):  # varre a lista e converte cada elemento para ponto flutuante
        a.append(float(pilhaNumeros.pop(0)))
    return a


def retirarPontos(pilhaOperadores):
    ponto = '.'
    while ponto in pilhaOperadores:
        pilhaOperadores.remove(ponto)
    return pilhaOperadores


def executaComando(pilhaNumeros, pilhaOperadores):  # recebe uma pilha de numeros e uma pilha de operadores

    if len(pilhaNumeros) > len(pilhaOperadores):
        a = []
        a.append(pilhaNumeros.pop(0))
    else:
        a = []

    while len(pilhaNumeros) > 0:
        if pilhaOperadores[0] == '+':
            pilhaOperadores.pop(0)
            a.append(pilhaNumeros.pop(0))
        elif pilhaOperadores[0] == '-':
            pilhaOperadores.pop(0)
            a.append(pilhaNumeros.pop(0) * -1)
    soma = 0
    for i in range(len(a)):
        soma += a.pop(0)
    return soma


comando = input(">>>DIGITE O COMANDO: ").lower()  # Pede Comando
while comando != "sair":  # Loop para sempre pedir o comando

    try:
        pilhaNumeros = converterString(
            numeros(comando, "+-"))  # tenta empilhar os números, caso não consiga ele prossegue
    except (RuntimeError, TypeError, NameError, ValueError):
        pass

    try:
        pilhaOperadores = operadores(comando)
    except (
    RuntimeError, TypeError, NameError, ValueError):  # tenta empilhar os operadores, caso não consiga ele prossegue
        pass

    try:
        pilhaOperadores = retirarPontos(pilhaOperadores)
    except (
    RuntimeError, TypeError, NameError, ValueError):  # tenta empilhar os operadores, caso não consiga ele prossegue
        pass

    try:
        print(executaComando(pilhaNumeros,
                             pilhaOperadores))  # tenta executar o comando do usuário, caso não consiga ele retorna comando inválido
    except NameError:
        print("COMANDO INVÁLIDO")

    comando = input(">>>DIGITE O COMANDO: ").lower()  # pede o comando novamente