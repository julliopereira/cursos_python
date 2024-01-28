"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

# print(1)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6_7 = soma(4, 5, 6, 7)
print(soma_4_5_6_7)

numeros = 1, 2, 3, 4, 5, 6      # isto é uma TUPLA

soma_1_a_6 = soma(*numeros)
print(soma_1_a_6)


print(sum(numeros))