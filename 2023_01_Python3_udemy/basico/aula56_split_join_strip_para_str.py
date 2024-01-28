import os

"""
split e join com list e str
split - divide uma string
join - une uma string

"""

frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i])
    lista_frases[i] = lista_frases[i].strip()       # tira os espaços a esq. e dir.
    print(lista_frases[i])

print(lista_frases)

print('-'*80)

frases_unidas = ','.join(lista_frases)      # join une dois interaveis, nesse caso com virgula
print(frases_unidas)





