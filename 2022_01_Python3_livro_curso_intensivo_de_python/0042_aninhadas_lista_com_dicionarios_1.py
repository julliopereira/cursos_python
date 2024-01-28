### EXPLICAÇÃO.

'''
Muitas vezes você quer adicionar um dicionarío como valor de uma lista, 
ou seja, em uma posição de uma lista você pode ter várias informações 
contidas em um dicionário.

'''

# DICIONARIOS:

pessoa_1 = {'nome': 'rodrigo', 'idade': '20', 'altura': '1.70', 'peso': '70'}
pessoa_2 = {'nome': 'maria', 'idade': '24', 'altura': '1.66', 'peso': '65'}
pessoa_3 = {'nome': 'sara', 'idade': '23', 'altura': '1.68', 'peso': '71'}

# ADICIONANDO Ã LISTA:

lista = (pessoa_1, pessoa_2, pessoa_3)
for pessoa in lista:
    print(pessoa)

