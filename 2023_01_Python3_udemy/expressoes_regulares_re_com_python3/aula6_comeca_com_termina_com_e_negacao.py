# Metacaracteres:
# ^ = comeca com 
# $ = termina com 
# [^a-z] = negacao

import re

# cpf = 'a 234.645.123-23'

# print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)) # nao pega nada porque nao comeca com cpf

# cpf = '234.645.123-23 qualquer coisa'

# print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)) # bate porque comeca com cpf


cpf = '234.645.123-23'

print(re.findall(r'[^0-9]+', cpf)) # negando o conjunto de 0-9 (numeros)


