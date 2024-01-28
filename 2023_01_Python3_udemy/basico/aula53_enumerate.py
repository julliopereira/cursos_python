
"""
enumerate - enumera iteráveis (índices)
numera cada indice da sua lista
"""

# [(0,'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'joao')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('joao')

# lista_enumerada = enumerate(lista)

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print(f'FOR da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

