def numeros(s, sep): #recebe como parametro uma String e os separadores
    pilha = [s] #inicia uma pilha com a String passada
    for i in sep: #varre a string e remove cada separador encontrado
        pedaco = []
        for j in pilha:
            pedaco.extend(j.split(i))
        pilha = pedaco
    return pilha #retorna a pilha agora sem separador

def operadores(s): #recebe como parametro uma String
    semNumero = [] #inicia uma lista vazia
    for i in s: #varre a lista atras de digito, caso não seja digito é adcionado a lista
        if not i.isdigit():
            semNumero.append(i)
    return semNumero #retorna lista

def converterString(pilhaNumeros): #recebe uma lista de string
    a = [] #inicia uma lista vazia
    for i in range(len(pilhaNumeros)): #varre a lista e converte cada elemento para ponto flutuante
        a.append(float(pilhaNumeros.pop(0)))
    return a

def executaComando(pilhaNumeros, pilhaOperadores): #recebe uma pilha de numeros e uma pilha de operadores
    a = pilhaNumeros[0]
    pilhaNumeros.pop(0)
    while len(pilhaNumeros) >= 1 and len(pilhaOperadores) > 0: #enquanto a pilha de números ainda tiver itens e a de operadores não estiver vazia, uma operação será realizada
        if pilhaOperadores[0] == "+": #comparação com operador
            if len(pilhaNumeros) > 0:
                a += pilhaNumeros[0]
                pilhaNumeros.pop(0) #desempilha um número
        elif pilhaOperadores[0] == "-":
            if len(pilhaNumeros) > 0:
                a -= pilhaNumeros[0]
                pilhaNumeros.pop(0) #desempilha um número
        elif pilhaOperadores[0] == ".":
            pilhaOperadores.pop(0) #desempilha o operador
            continue
        else:
            print("COMANDO INVALIDO") #Retorna comando invalido caso nenhuma condição seja atingida.
        pilhaOperadores.pop(0)
    return a


comando = input(">>>DIGITE O COMANDO: ").lower() #Pede Comando
while comando != "sair": #Loop para sempre pedir o comando

    try:
        pilhaNumeros = converterString(numeros(comando, "+-")) #tenta empilhar os números, caso não consiga ele prossegue
    except (RuntimeError, TypeError, NameError, ValueError):
        pass

    try:
        pilhaOperadores = operadores(comando)
    except (RuntimeError, TypeError, NameError, ValueError): #tenta empilhar os operadores, caso não consiga ele prossegue
        pass

    try:
        print(executaComando(pilhaNumeros, pilhaOperadores)) #tenta executar o comando do usuário, caso não consiga ele retorna comando inválido
    except NameError:
        print("COMANDO INVÁLIDO")

    comando = input(">>>DIGITE O COMANDO: ").lower() #pede o comando novamente