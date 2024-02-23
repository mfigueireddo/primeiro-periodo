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

# Validação do número 1

numero_1 = input("Insira um número: ")

while eh_numero(numero_1) ==  False:
    print("\nInsira apenas números")
    numero_1 = input("Insira um número: ")

# Validação do operador

print("\nLista de operadores: +, -, *, /, **, //, %")
operador = input("Insira o operador: ")

while eh_operador(operador) ==  False:
    print("\nInsira um operador válido.")
    operador = input("Insira o operador: ")

# Validação do número 2

numero_2 = input("\nInsira outro número: ")

while eh_numero(numero_2) ==  False:
    print("\nInsira apenas números.")
    numero_2 = input("Insira outro número: ")

if operador == "/" or operador == '//' or operador == '%':
    while float(numero_2) == 0:
        print("\nNão é possível realizar operações de divisão por 0.")
        numero_2 = input("Insira outro número: ")

# Contas
        
numero_1 = float(numero_1)
numero_2 = float(numero_2)
    
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

# Imprimindo o resultado
    
print("\n%.2f %s %.2f = %.2f" %(numero_1,operador,numero_2,resultado))