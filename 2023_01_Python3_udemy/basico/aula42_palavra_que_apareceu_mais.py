frase = 'O Python é uma linguagem de rogramação' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum'

# print(frase.count('Python'))            # Conta quantas vezes a palavra Python apareceu no texto

i = 0
qde_vezes_letra_apareceu = 0
letra_apareceu_meis_vezes = 0

while i < len(frase):                      # enquanto i menor que o tamanho de letras da frase
    letra_atual = frase[i]                 # guardar valor da letra na variavel letra_atual
    qe_letra_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue 

    if qde_vezes_letra_apareceu < qe_letra_atual:
        qde_vezes_letra_apareceu = qe_letra_atual
        letra_apareceu_meis_vezes = letra_atual

    #print(letra_atual, vezes_letra_apareceu)                     # mostra a letra atual
    i += 1                                 # soma mais 1 a letra a i 

print(f'A letra "{letra_apareceu_meis_vezes}" '
      f'apareceu {qde_vezes_letra_apareceu}x')