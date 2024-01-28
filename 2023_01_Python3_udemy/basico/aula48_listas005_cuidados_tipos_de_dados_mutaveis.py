"""
Cuidadoscom dados mutaveis
= -  copiado o valor (imutaveis)
+ -  aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a                   # copiar lista a 

print(lista_b)

lista_a[0] = 'outro valor'          # alterado valor na lista a

print(lista_b)                      # valor tambem alterado na lista b

print('-'*50)

lista_b = lista_a.copy()            # Copia a lista_a tornando totalmente b independente

lista_a[0] = 'alterado a'

print(lista_a)
print(lista_b)

