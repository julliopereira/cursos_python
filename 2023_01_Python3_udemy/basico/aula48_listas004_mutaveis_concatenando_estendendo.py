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

lista_a = [1,2,3]
lista_b = [3,4,5]

lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)       # estende a lista a com os valores da lista b
print('Listas a e b concatenadas\t',lista_c)
print('Lista a extendida\t\t',lista_a)

