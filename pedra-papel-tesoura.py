import random

def valida_escolha(escolha_usuario):

    while escolha_usuario not in ['1','2','3']:
        
        print("\nInsira uma opção válida.")
        escolha_usuario = input("Insira o número de sua escolha: ")

    return int(escolha_usuario)

def pedra(escolha_computador):
    if escolha_computador == 3:
        return 0
    elif escolha_computador == 2:
        return 1
    elif escolha_computador == 1:
        return 2
 
def papel(escolha_computador):
    if escolha_computador == 1:
        return 0
    elif escolha_computador == 3:
        return 1
    elif escolha_computador == 2:
        return 2

def tesoura(escolha_computador):
    if escolha_computador == 2:
        return 0
    elif escolha_computador == 1:
        return 1
    elif escolha_computador == 3:
        return 2

def imprime_resultado(resultado):
    if resultado == 0:
       print("\nParabéns, você ganhou!")
    elif resultado == 1:
       print("\nVocê perdeu.")
    elif resultado == 2:
       print("\nHouve um empate")

def int_string(numero):
    if numero == 1:
        return "Pedra"
    elif numero == 2:
        return "Papel"
    else:
        return "Tesoura"

def valida_fim(escolha_fim):

    while escolha_fim not in ['1', '2']:

        print("\nInsira uma opção válida.")
        escolha_fim = int(input("Gostaria de jogar de novo? (1) Sim (2) Não"))

    if escolha_fim == '1':
        return False
    
    return True

fim = False

while fim == False:

    print("Opções: (1) pedra, (2) papel, (3) tesoura.")

    escolha_usuario = input("Insira o número de sua escolha: ")

    escolha_usuario = valida_escolha(escolha_usuario)

    escolha_computador = random.randint(1,3)

    if escolha_usuario == 1:
        resultado = pedra(escolha_computador)
    elif escolha_usuario == 2:
        resultado = papel(escolha_computador)
    else:
        resultado = tesoura(escolha_computador)

    imprime_resultado(resultado)
    print("Você escolheu %s e o computador escolheu %s." %(int_string(escolha_usuario),int_string(escolha_computador)))

    escolha_fim = input("\nGostaria de jogar de novo? (1) Sim (2) Não ")
    fim = valida_fim(escolha_fim)
    print("")