"""
Operadores de atribuicao
= += -= *= /= //= **= %=
"""

contador = 1

# while contador < 10:
#     print(contador)
#     contador = contador + 1

# print('Acabou')

contador += 1           # mesma coisa que contador = contador + 1
print(contador)

contador *= '2'         # repetir o numero 2 tantas vezes o numero atribuido ao numero contador e atri
print(contador)           # buir a variavel contador

contador = int(contador)# voltar contador como inteiro
contador %= 2           # atibuir o modulo de valor do contador modulo de 2 a variavel contador
print(contador)           

contador = 20           # retornar um valor a variavel contador

contador //= 2          # divisao sem ponto flutuante
print(contador)  

contador /= 2           # divisao com ponto flutuante
print(contador)  

contador **= 2          # exponencição
print(contador)  

