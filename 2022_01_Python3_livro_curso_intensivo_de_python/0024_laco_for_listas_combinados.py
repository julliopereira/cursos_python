### EXIBIR NUMEROS DE 1 A 20

print(range(1, 21))

print('-'*50)
### CRIAR LISTA DE 1 - 1000000 E UM LAÇO PARA EXIBI-LOS 

digitos = list(range(1, 1000001))
'''
# REMOVER COMENTARIO PARA VER VALOR
for d in digitos:
    print(d)
'''

print('-'*50)
### UTILIZE min max e sum  E MOSTRE
print(min(digitos))
print(max(digitos))
print(sum(digitos))

print('-'*50)
### CRIAR LISTA NUMEROS DE 1 A 10 ELEVE AO CUBO CADA UM E MOSTRE
cubo =  [valor**3 for valor in range(1, 11)]
print(cubo)


