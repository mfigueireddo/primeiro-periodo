import random

def escolha_palavra():

    palavras = ["rinoceronte","basquete","ventilador"]
    palavra_secreta = random.choice(palavras)

    return palavra_secreta

def indices(palavra_secreta,chute):

    # Cria uma lista que irá retornar o(s) índice(s) do chute na palavra secreta
    indices = []
    auxiliar_indice = -1
    contador = 0

    # Conta quantas vezes o chute apareceu na palavra
    frequencia = palavra_secreta.count(chute)

    while contador < frequencia:
        # Adiciona na lista o índice do chute na palavra (podendo ser mais de uma)
        indices += [palavra_secreta.find(chute,auxiliar_indice+1)]
        auxiliar_indice = indices[contador]
        contador += 1

    # Retorna uma lista com os índices
    return indices

def valida_chute(chute,letras_chutadas):

    while chute in letras_chutadas:
        print("\nVocê já chutou esta letra.")
        chute = input("Chute uma letra: ")

    return chute

def acerto(chute,palavra_secreta,desenho):

    print("%s está na palavra!" %(chute))

    # Chama a função que retorna o(s) índice(s) onde aparece o chute
    lista = indices(palavra_secreta,chute)

    # Percorre a lista de índice(s)
    for elemento in lista:

        # Transforma a letra em maiúscula caso seja a primeira letra da palavra
        if elemento == 0:
            chute = chute.upper()

        # Altera o _ pelo chute
        desenho[elemento] = chute

    return desenho

def erro(chances):

    print("\n%s não está na palavra." %(chute))

    return chances - 1

def informativo(chances,desenho,letras_chutadas):

    print("\nVocê tem %d chances!" %(chances))

    print(*desenho)

    print("Letras chutadas: ", end="")
    print(*letras_chutadas, sep=" ")

def resultado(vitoria):

    if vitoria == 1:
        print("\nParabéns, você ganhou!")
        print("Você adivinhou a palavra %s em %d chutes!" %(palavra_secreta, quantidade_chutes))

    else :
        print("\nVocê perdeu.")
        print("A palavra correta era %s." %(palavra_secreta))

def valida_fim(escolha_fim):

    while escolha_fim not in ['1', '2']:

        print("Insira uma opção válida.")
        escolha_fim = int(input("Gostaria de jogar de novo? (1) Sim (2) Não"))

    if escolha_fim == '1':
        return False
    
    return True

fim = False

while fim == False:

    palavra_secreta = escolha_palavra()

    vitoria = 0

    tamanho = len(palavra_secreta)
    chances = tamanho/2

    letras_chutadas = []
    quantidade_chutes = 0

    # Cria uma string com _ para representar espaços vazios na palavra
    desenho = ["_"] * tamanho

    print("Você tem %d chances!" %(chances))
    print(*desenho)

    while chances != 0:
        chute = input("\nChute uma letra: ")
        chute = chute.lower()

        chute = valida_chute(chute,letras_chutadas)

        quantidade_chutes += 1
        letras_chutadas += chute

        # Em caso de acerto
        if chute in palavra_secreta:
            desenho = acerto(chute,palavra_secreta,desenho)

        # Em caso de erro
        else:
            chances = erro(chances)

        # Revela o usuário quantas chances lhe restaram, o estado do desenho e as letras chutadas
        informativo(chances,desenho,letras_chutadas)

        # Condição de vitória
        if "_" not in desenho:
            vitoria = 1
            break

    # Imprime o resultado
    resultado(vitoria)

    escolha_fim = input("\nGostaria de jogar de novo? (1) Sim (2) Não ")
    fim = valida_fim(escolha_fim)
    print("")