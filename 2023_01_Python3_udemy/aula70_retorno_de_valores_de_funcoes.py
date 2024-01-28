"""
Retorno de valores das funções (return)
"""

# exemplo 1
# def soma(x, y):
#     return x + y        # Se não for aditionado a funcao retorna None por default
#     # print(x + y)      # Nenhum codigo sera analisado após return (ele para o codigo no return)

# soma1 = soma(2, 2)
# soma2 = soma(3, 3)

# print(soma1 + soma2)

#--------------------------------------------------------------------------

# exemplo 2
def soma(x, y):
    if x > 10:
        return 10       # Se x maior que 10 retorna 10 e -PÁRA O CODIGO-
    return x + y        # Se não for aditionado a funcao retorna None por default

soma1 = soma(11, 2)
soma2 = soma(3, 3)

print(soma1 + soma2)

