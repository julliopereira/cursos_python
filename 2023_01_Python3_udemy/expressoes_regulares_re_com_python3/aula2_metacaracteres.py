# Não conseguimos utilizar metacaracteres de forma literal, precisamos escapar
#
# META caracteres: . ^ $ * + { } [ ] \ | ( )
#
# |   = ou
# .   = qualquer caracteres na posicao onde esta o ponto
# []  = conjunto de caracteres
# 


import re

texto = '''
Julio foi ao parque hoje pela manhã andar de bicicleta. Chegando lá avistou seus amigos de infância 
e decidiu falar com eles. 
Olá pessoal tudo bem ? lembram de mim ? Sou o Julio que jogava bola com vocês na rua em frente de 
casa. 


Eles rapidamente lembraram pois realmente, nós não saíamos da rua. Jogavamos bola todos os dias 
um chamando o outro e brigando com a mãe um do outro até que conseguissemos nosso objetivo. 
Passamos a conversar sobre essa época e por fim o que estamos fazendo agora. Todos com seu dia-a-dia
interessantíssimos!. 
Enfim acabamos nossa conversa já pela noite, já era hora de ir para cama, cada um de nós. Agora somos
trabalhadores e movemos um país assim como nossos antepassados. Eu sou julio! ;-)
'''

# exemplo com |
print(re.findall(r'Julio|frente', texto))   # Julio ou frente

# exemplo com . 
print(re.findall(r'Julio|fr..te|an.......dos', texto))   # Julio ou fr..te ou antepassados

# exemplo com []
print(re.findall(r'[Jj]ulio', texto))   # Julio ou julio ; ou seja, ou com J ou j
print(re.findall(r'[a-z]ulio', texto))   # julio - somente os que estiverem entre a-z minusculos
print(re.findall(r'[A-Z]ulio', texto))   # Julio - somente os que estiverem entre A-Z maiusculos
print(re.findall(r'julio', texto, flags=re.IGNORECASE))   # Julio - ignorando case, ou seja, tanto faz maiusculo ou minusculo

