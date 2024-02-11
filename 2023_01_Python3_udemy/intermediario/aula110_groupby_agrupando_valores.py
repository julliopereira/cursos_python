# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [ 
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Julio', 'nota': 'B'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Marcela', 'nota': 'C'},
    {'nome': 'Gabriela', 'nota': 'D'},
    {'nome': 'Rubens', 'nota': 'E'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'Joao', 'nota': 'A'},
]


# -ORDENAR DICIONARIO- 

alunos_agrupados = sorted(alunos, key=lambda x: x['nota'])
grupos = groupby(alunos_agrupados, key=lambda x: x['nota'])

for chave, grupo in grupos:
    print(chave)
    # print(list(grupo))
    for aluno in grupo:
        print(aluno)



# ---------------------------------------------------------------------
# - PRIMEIRA EXPLICACAO- 
# alunos = ['a', 'a', 'a','b', 'c', 'b', 'a', 'c', 'a']   
# grupos = groupby(sorted(alunos))

# for chave, grupos in grupos:
#     print(chave)
#     print(list(grupos))