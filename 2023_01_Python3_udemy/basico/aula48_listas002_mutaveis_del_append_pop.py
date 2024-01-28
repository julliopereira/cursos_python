"""
Listas em Python
Tipo list - mutáveis
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis:
    Append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, let, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]                              # deleta valor na posicao 2
# print(lista)
# print(lista[2])

lista.append(50)                            # adiciona no final da lista
lista.pop()                                 # remove o ultimo valor da lista 
ultimo_valor = lista.pop()                  # remove valor e atribuir em variavel para ver depois
ultimo_valor = lista.pop(2)                 # remove o valor do item3 
print(lista, 'Removido', ultimo_valor)

