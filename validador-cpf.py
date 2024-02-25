def remove_pontos(cpf):
    cpf = cpf.replace('.','')
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')
    return cpf

def adiciona_pontos(cpf):
    cpf = cpf[:3] + '.' + cpf[3:]
    cpf = cpf[:7] + '.' + cpf[7:]
    cpf = cpf[:11] + '-' + cpf[11:]
    return cpf

def eh_numero(string):

    for elemento in string:
        caracter = ord(elemento)

        if caracter<48 or caracter>57:
            return False
    
    return True

def valida_formatacao(cpf):

    while len(cpf) != 14 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        print("\nFormatação inválida.")
        print("Formato: 123.456.789-10")
        cpf = input("Insira seu CPF: ")

    cpf = remove_pontos(cpf)
    return cpf

def valida_numero(numero):

    while eh_numero(numero) == False:

        print("\nInsira apenas números.")
        numero = input("Insira um número: ")

    numero = adiciona_pontos(numero)
    return numero

def valida_cpf(numero):

    numero = valida_formatacao(numero)
    numero = valida_numero(numero)

    return numero

def peso_algarismos(cpf):

    soma = 0

    if len(cpf) == 9:
        for x in range(1,10):
            soma += int(cpf[x-1]) * x
        return soma
    
    else:
        for x in range(0,10):
            soma += int(cpf[x]) * x
        return soma 

def resto(soma):
    resto = soma % 11
    if resto == 10:
        return '0'
    return str(resto)
    
def valida_fim(escolha_fim):

    while escolha_fim not in ['1', '2']:

        print("\nInsira uma opção válida.")
        escolha_fim = int(input("Gostaria de jogar de novo? (1) Sim (2) Não"))

    if escolha_fim == '1':
        return False
    
    return True

fim = 0

while fim == 0:

    print("Formato: 123.456.789-10")
    cpf_usuario = input("Insira seu CPF: ")
    cpf_usuario = valida_cpf(cpf_usuario)
    cpf_validado = remove_pontos(cpf_usuario)
    cpf_validado = cpf_validado[:-2]

    soma = peso_algarismos(cpf_validado)
    primeiro_digito = resto(soma)
    cpf_validado += primeiro_digito

    soma = peso_algarismos(cpf_validado)
    segundo_digito = resto(soma)
    cpf_validado += segundo_digito

    cpf_validado = adiciona_pontos(cpf_validado)

    if cpf_validado == cpf_usuario:
        print("Seu CPF é válido.")
    else:
        print("Seu CPF é inválido. O correto seria %s." %(cpf_validado))

    escolha_fim = input("\nGostaria de usar novamente? (1) Sim (2) Não ")
    fim = valida_fim(escolha_fim)
    print("")