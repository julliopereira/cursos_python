"""
Iterando strings com while
"""

#.......0123456789101112
nome = 'Julio Pereira'        # Iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[3:8])

# faca codigo para escrever *J*u*l*i*o* *P*e*r*e*i*r*a*

qde_letras = len(nome)
contador = 0
nova_string = ''

while contador < qde_letras:
    nova_string += '*'
    letra = nome[contador]
    nova_string += letra
    contador += 1

print(f'{nova_string=}')
