'''
Função lambda em Python
A função lambda é uma função como qualquer outra em Python
Porém, são funções anônimas que contém apenas uma linha. 
Ou seja, tudo deve ser contido dentro de uma única expressão.
lista = [
    {'nome': 'Julio', 'sobrenome': 'Cesar'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Pedro', 'sobrenome': 'Moreira'},
    {'nome': 'Jose', 'sobrenome': 'Souza'},
    {'nome': 'Aline', 'sobrenome': 'Moreto'},
]
'''

# exemplo 1
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# # lista.sort()                              # ordena
# lista.sort(reverse=True)                  # ordena inversamente
# # sorted(lista)                               # copia raza

# print(lista)

# exemplo 2

lista = [
    {'nome': 'Julio', 'sobrenome': 'Cesar'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Pedro', 'sobrenome': 'Moreira'},
    {'nome': 'Jose', 'sobrenome': 'Souza'},
    {'nome': 'Aline', 'sobrenome': 'Moreto'}
]

# def ordena(item):
#     # return item['sobrenome']
#     return item['nome']

# lista.sort(key=ordena)

# for item in lista:
#     print(lista)

# final
def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])


exibir(l1)
exibir(l2)