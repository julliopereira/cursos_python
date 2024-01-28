
"""
Tipo de tupla - Uma lista imutável
Mais rápida que LISTA
>> usado sem colchetes <<
>> tupla tambem pode ser montada com parenteses <<
"""

nomes = 'Maria', 'Helena', 'Luiz'           # Isso é uma Tupla
nomes2 = ('Maria', 'Helena', 'Luiz')        # Isso também é uma Tupla
print(nomes[0])
print(nomes[-1])
print(nomes2[1])

lista = ['jose', 'armindeo', 'rafael']
print(f'lista: ',type(lista))
tupla = tuple(lista)                        # Inverte de LISTA para TUPLA
print(f'tupla: ',type(tupla))
lista2 = list(tupla)                        # Inverte de TUPLA para LISTA
print(f'tupla: ',type(lista2))