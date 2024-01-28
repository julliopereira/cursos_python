# Operadores lógicos
# String são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'
#print(nome[2])
#print(nome[-4])
#print('á' in nome)  # se á estiver dentro de nome True
#print( 'zero' in nome) # zero não está em nome entao False

nome = input('Digiite seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar}  existe em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
