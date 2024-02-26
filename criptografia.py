def criptografia(mensagem):

    for indice, elemento in enumerate(mensagem):

        maiuscula = False
        minuscula = False

        elemento_asciii = ord(elemento)

        if elemento_asciii >= 65 and elemento_asciii <= 90:
            maiuscula = True
            minuscula = False

        elif elemento_asciii >= 97 and elemento_asciii <= 122:
            maiuscula = False
            minuscula = True

        if maiuscula or minuscula:

            letra_criptografada = elemento_asciii+3

            if (maiuscula and elemento_asciii+3 > 90) or (minuscula and elemento_asciii+3 > 122):
                letra_criptografada -= 26
            
            mensagem = mensagem[:indice] + chr(letra_criptografada) + mensagem[indice+1:]

    return mensagem

def valida_fim(escolha_fim):

    while escolha_fim not in ['1', '2']:

        print("\nInsira uma opção válida.")
        escolha_fim = int(input("Gostaria de jogar de novo? (1) Sim (2) Não"))

    if escolha_fim == '1':
        return False
    
    return True

fim = 0

while fim == 0:

    input_usuario = input("Insira uma mensagem: ")

    input_usuario = criptografia(input_usuario)

    print("Sua mensagem criptografada é: %s" %(input_usuario))

    escolha_fim = input("\nGostaria de usar novamente? (1) Sim (2) Não ")
    fim = valida_fim(escolha_fim)
    print("")