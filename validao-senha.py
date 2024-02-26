def validacao_senha(senha):

    presenca_maiusculas = 0
    presenca_minusculas = 0
    presenca_numeros = 0

    for algarismo in senha:
        if ord(algarismo)>=65 and ord(algarismo)<=90:
            presenca_maiusculas = 1
        if ord(algarismo)>=97 and ord(algarismo) <= 122:
            presenca_minusculas = 1
        if ord(algarismo) >= 48 and ord(algarismo) <= 57:
            presenca_numeros = 1

    print("\n",end="")
    if len(senha)<8:
        print("Senha inválida: mínimo de 8 caracteres.")
    if presenca_maiusculas == 0:
        print("Senha inválida: mínimo de 1 letra maiúscula.")
    if presenca_minusculas == 0:
        print("Senha inválida: mínimo de 1 letra minúscula.")
    if presenca_numeros == 0:
        print("Senha inválida: mínimo de 1 número.")

    while len(senha) < 8 or presenca_maiusculas == 0 or presenca_minusculas == 0 or presenca_numeros == 0:

        senha = input("Insira sua senha: ")

        presenca_maiusculas = 0
        presenca_minusculas = 0
        presenca_numeros = 0

        for algarismo in senha:
            if ord(algarismo)>=65 and ord(algarismo)<=90:
                presenca_maiusculas = 1
            if ord(algarismo)>=97 and ord(algarismo) <= 122:
                presenca_minusculas = 1
            if ord(algarismo) >= 48 and ord(algarismo) <= 57:
                presenca_numeros = 1

        print("\n",end="")
        if len(senha)<8:
            print("Senha inválida: mínimo de 8 caracteres.")
        if presenca_maiusculas == 0:
            print("Senha inválida: mínimo de 1 letra maiúscula.")
        if presenca_minusculas == 0:
            print("Senha inválida: mínimo de 1 letra minúscula.")
        if presenca_numeros == 0:
            print("Senha inválida: mínimo de 1 número.")

    return senha

print("Requisitos\n- Ao menos 8 dígitos\n- Ao menos uma letra maiúscula\n- Ao menos uma letra maiúscula\n- Ao menos um número")

input_usuario = input("Insira sua senha: ")
input_usuario = validacao_senha(input_usuario)

print("\nSua senha corresponde aos requisitos.")