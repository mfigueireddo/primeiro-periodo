import random

def eh_numero(string):

    for elemento in string:
        caracter = ord(elemento)

        if caracter<48 or caracter>57:
            return False
    
    return True

def valida_numero(numero):

    while eh_numero(numero) == False:

        print("\nInsira apenas números.")
        numero = input("Insira um número: ")

    return int(numero)

def valida_chute(numero):

    numero = valida_numero(numero)

    while numero < 1 or numero > 9:
        print("\nInsira um número entre 0 e 10.")
        numero = input("Insira um número: ")
        numero = valida_numero(numero)

    return numero

def valida_fim(escolha_fim):

    while escolha_fim not in ['1', '2']:

        print("\nInsira uma opção válida.")
        escolha_fim = int(input("Gostaria de jogar de novo? (1) Sim (2) Não"))

    if escolha_fim == '1':
        return False
    
    return True

def resultado(vitoria,numero_secreto,quantidade_chutes):

    if vitoria == 1:
        print("\nParabéns, você ganhou!")
        print("Você adivinhou o número %d em %d chutes!" %(numero_secreto, quantidade_chutes))

    else :
        print("\nVocê perdeu.")
        print("O número correto era %d." %(numero_secreto))

print("Adivinhe o número secreto que está entre 0 e 10!")

fim = 0

while fim == 0:

    chances = 10
    quantidade_chutes = 0
    vitoria = 0
    numero_secreto = random.randint(1,9)

    while chances > 0:

        chute = input("Insira seu chute: ")
        chute = valida_chute(chute)
        quantidade_chutes += 1

        if chute == numero_secreto:
            print("\nVocê acertou! O número secreto é %d!" %(numero_secreto))
            vitoria = 1
            break
        elif chute < numero_secreto:
            print("\nO número secreto é maior que %d." %(chute))
            chances -= 1
        else:
            print("\nO número secreto é menor que %d." %(chute))
            chances -= 1

        print("\nVocê tem %d chances." %(chances))

    resultado(vitoria,numero_secreto,quantidade_chutes)

    escolha_fim = input("\nGostaria de jogar de novo? (1) Sim (2) Não ")
    fim = valida_fim(escolha_fim)
    print("")