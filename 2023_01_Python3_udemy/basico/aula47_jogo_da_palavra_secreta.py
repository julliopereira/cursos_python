"""

"""
palavra_secreta = 'paralelepipedo'
tentativas = 0
qde_letras = 0
errou = 0
palavra = ''
while True:
    tentativas += 1
    print('-'*60)

    if tentativas == 1:
        print('Palavra Secreta: \n')
        print('_.'*len(palavra_secreta) + '\n')
    else:
        print('Palavra Secreta: \n')
        for l in palavra_secreta:
            if l == letra:
                print(l,'.',end='')
                qde_letras += 1
            else:
                print('_.',end='')
        print(palavra)

    letra = input('\n\nDigite uma letra: ')

    if len(letra) > 1:
        print('\n\n >>>> Digite apenas uma letra <<<< \n\n')
        continue

    if letra not in palavra_secreta:
        print(f'\n\n >>> Errou .... letra "{letra} não existe na palavra ..." \n\n')
        errou += 1
        continue

    if qde_letras == len(palavra_secreta)-1:
        break

print(f'\n\n\nVocê tentou "{tentativas}" vezes para descobrir a palavra secreta "{palavra_secreta}" \nerrou "{errou}" vezes')

