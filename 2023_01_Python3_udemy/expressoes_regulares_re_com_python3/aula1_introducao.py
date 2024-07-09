# explicação RE

import re

# findall(todos os encontros) | search(match) | sub (substituir)
# compile(compilar) reutilizar
# é case sensitive 

string = 'Este é um teste de expressões teste regulares.'

# print(re.search(r'teste', string))      # verifica so a primeira ocorrencia; encontrou para!

# print(re.findall(r'teste', string))     # verifica todas as ocorrencias

# print(re.sub(r'teste', 'abcd', string))         # substitui por abcd

# print(re.sub(r'abcd', 'teste', string, count=1))         # substitui por abcd apenas uma vez


#-------------------------------------------------------

regexp = re.compile(r'teste')       # usando compile pode utilizar varias vezes a palavra procurada

print(regexp.search(string))        # usando com search
print(regexp.findall(string))       # usando com findall
print(regexp.sub('DEF', string))    # usando com sub