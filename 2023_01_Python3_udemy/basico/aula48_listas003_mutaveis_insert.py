"""
Listas em Python
Tipo list - mutáveis
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis:
    append  -   Adiciona um item ao final 
    insert  -   Adiciona um item no indice escolhido 
    pop     -   Remove do final ou do índice escolhio
    del     -   Apaga um índice
    clear   -   Limpa a lista
    extend  -   Estende a lista
    +       -   Concatena listas
Create Read Update   Delete
Criar, let, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]

del lista[-1]                   # Deleta o último valor da lista
lista.insert(0,5)               # Inserir valor passando "indice, valor" (insere e move o restante)
lista.insert(100, 'indice')     # Nao existe indice 100 ou 99, adiciona no ultimo
print(lista)
lista.clear()                   # limpa a lista
