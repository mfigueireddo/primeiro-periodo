# Calculadora utizando o terminal para pedir as instruções do usuário
# As instruções serão recebidas no formato de string para validação
# A validação será feito com base nos valores da tabela ASCII

def eh_numero(string):

    for elemento in string:
        caracter = ord(elemento)

        if caracter<48 or caracter>57:
            return False
    
    return True

def eh_operador(string):

    operadores = ['+','-','*','/','**','//','%']

    if string not in operadores:
        return False
    
    return True

def valida_numero(numero):

    while eh_numero(numero) ==  False:

        print("\nInsira apenas números")
        numero = input("Insira um número: ")

    return numero

def valida_operador(operador):

    while eh_operador(operador) ==  False:
        print("\nInsira um operador válido.")
        operador = input("Insira o operador: ")

    return operador

def soma(numero_1,numero_2):

    return numero_1 + numero_2

def subtracao(numero_1,numero_2):

    return numero_1 - numero_2

def multiplicacao(numero_1,numero_2):

    return numero_1 * numero_2

def divisao(numero_1,numero_2):

    return numero_1 / numero_2

def potenciacao(numero_1,numero_2):

    return numero_1 ** numero_2

def parte_inteira(numero_1,numero_2):

    return numero_1 // numero_2

def resto(numero_1,numero_2):

    return numero_1 % numero_2

def contas(numero_1,numero_2,operador):

    if operador == '+':
        resultado = soma(numero_1,numero_2)

    elif operador == '-':
        resultado = subtracao(numero_1,numero_2)
    
    elif operador == '*':
        resultado = multiplicacao(numero_1,numero_2)
    
    elif operador == '/':
        resultado = divisao(numero_1,numero_2)
    
    elif operador == '**':
        resultado = potenciacao(numero_1,numero_2)
    
    elif operador == '//':
        resultado = parte_inteira(numero_1,numero_2)
    
    elif operador == '%':
        resultado = resto(numero_1,numero_2)

    return resultado

def valida_fim(escolha_fim):

    while escolha_fim not in ['1', '2']:

        print("Insira uma opção válida.")
        escolha_fim = int(input("Gostaria de jogar de novo? (1) Sim (2) Não"))

    if escolha_fim == '1':
        return False
    
    return True

fim = False

while fim == False:

    # Pede o primeiro número
    numero_1 = input("Insira um número: ")
    numero_1 = valida_numero(numero_1)

    # Pede o operador
    print("\nLista de operadores: +, -, *, /, **, //, %")
    operador = input("Insira o operador: ")
    operador = valida_operador(operador)

    # Pede o segundo número
    numero_2 = input("\nInsira outro número: ")
    numero_2 = valida_numero(numero_2)

    # Confere se não está sendo realizada uma divisão por 0
    if operador == "/" or operador == '//' or operador == '%':
        while float(numero_2) == 0:
            print("\nNão é possível realizar operações de divisão por 0.")
            numero_2 = input("Insira outro número: ")

    # Contas
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
        
    # Resultado
    resultado = contas(numero_1,numero_2,operador)
    print("\n%.2f %s %.2f = %.2f" %(numero_1,operador,numero_2,resultado))

    escolha_fim = input("\nGostaria de continuar? (1) Sim (2) Não ")
    fim = valida_fim(escolha_fim)
    print("")