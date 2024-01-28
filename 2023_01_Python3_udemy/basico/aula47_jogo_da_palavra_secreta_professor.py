

import os 

palavra_secreta = 'piracicaba'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('\n\nDigite uma letra: ')

    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('\n\n >>>> Digite apenas uma letra <<<< \n\n')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra Formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU !! PARABÉNS')
        print('A palavra era', palavra_formada)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
    

