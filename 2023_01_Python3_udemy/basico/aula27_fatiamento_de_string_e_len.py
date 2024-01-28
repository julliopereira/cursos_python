"""
Fatiamento de strings
012345678
Ola mundo
-987654321
Fatiamento [i:f:p] [::] (de/ate/passo)
Obs.: a funcao len retorna a qtd
de caracteres da str
"""

variavel = 'Ola mundo'  
print(variavel[4:])          # do 4 em diante
print(variavel[0:4])         # do 0 a 4 
print(len(variavel))         # conta quandidade caracteres da variavel
print(variavel[0:9:2])       # [de:ate:passo] (mostra as strings da posicao 0  ate a 9 pulando de 2 em 2)
print(variavel[-1:-10:-1])   # Inverter frase
print(variavel[::-1])        # Inverter frase tambem