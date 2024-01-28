'''
Exercicio - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função ser[a unir duas listas
na ordem.
Use todos os valores da menor lista.
Ex:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
'''

# # exercicio ===========================
# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i] , lista2[i]) for i in range(intervalo_maximo)
#     ]

# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(cidades, estados))

# funcao zip to python ===========================

from itertools import zip_longest   # o maior valor (zip usa o menor)

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))    # em uma lista
print(dict(zip(l1, l2)))    # em um dicionario

print(list(zip_longest(l1,l2, fillvalue='sem cidade'))) # usando o maior valor entre as listas


