"""
for in com listas
"""


lista = ['joaquim', 'jose', 'silva', 'maria', 'joao', 647]

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    indice += 1
