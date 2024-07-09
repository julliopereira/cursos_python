# Não conseguimos utilizar metacaracteres de forma literal, precisamos escapar
#
# META caracteres: ^ $ ( )
# *   = 0 OU N
# +   = 1 OU N
# ?   = 0 OU 1 
# {n}  
# {min, max}  
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
trabalhadores e movemos um país assim como nossos antepassados. Eu sou juuulioooo! ;-)
Boa tarrrrrrdeeeeeee !
'''

# exemplo com +
print(re.findall(r'Ju+lio+', texto, flags=re.I))   # O mais significa que pode aparecer UMA ou MAIS vezes.

print(re.sub(r'Ju+lio+', 'Luiz' ,texto, flags=re.I))   # Subtituir

# exemplo com ? 
print(re.sub(r'Ju?lio+', 'Luiz' ,texto, flags=re.I))   # u tem que nao repetir ou repetir uma vez, no caso repete mais que 1

# exemplo com {}
print(re.findall(r'Ju{1,}lio{1,}',texto, flags=re.I))   # {1,} o u repete uma ou mais vezes e tambem o o 
print(re.findall(r'Ju{1,}lio{10}',texto, flags=re.I))   # {10} especificamente 10
print(re.findall(r'Ju{1,}lio{2,10}',texto, flags=re.I))   # {2,10} de 2 a 10
print(re.findall(r'tar{6}de{1,40}',texto, flags=re.I))   # especifico



texto2 = 'João ama ser amado'


# exemplo com {} e *
print(re.findall(r'ama[do]{2}', texto2, flags=re.I))       # [do] uma letra dentro do quantificador, e {2} repete
print(re.findall(r'ama[do]*', texto2, flags=re.I))       # [do] uma letra dentro do quantificador, e *  repete 




