
"""
Introducao ao desempacotamento 
"""

# exemplo 1
# nomes = ['joaquim', 'jose', 'silva', 'marcelo']  
# nome1, nome2, nome3 = nomes           # tem valores a mais na lista 4
# print(nome2)                          # vai dar erro

# exemplo 2
# nome1, nome2, nome3 = ['joaquim', 'jose', 'silva']
# print(nome2)

# exemplo 3
# nome1, *resto = ['joaquim', 'jose', 'silva']    # empacota joaquim e guarda o restante em resto
# print(nome1, resto)                             # exibe o nome1 e o resto

# exemplo 4
_, nome2, *_ = ['joaquim', 'jose', 'silva']
print(nome2)