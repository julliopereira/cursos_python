
"""
CPF: 778.335.560-92
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva comçando de 10

Ex.:  778.335.560-92 (778335560)
      10  9  8  7  6  5  4  3  2  
*     7   7  8  3  3  5  5  6  0
    ------------------------------
      70  63 64 21 24 25 20 24 0


"""

import re   #expressao regular
import sys
import random


for _ in range(100):

    cpf_nove_dig = ''
    for i in range(9):
        cpf_nove_dig += str(random.randint(0, 9))

    soma = 0
    conta = 10

    for numero in cpf_nove_dig:
        resultado = conta * int(numero)
        soma = soma + resultado
        conta -= 1

    multiplica_por_dez = soma * 10
    conta = multiplica_por_dez % 11

    resultado_final = 0 if conta > 9 else conta


    cpf_dez_dig = int(cpf_nove_dig) + resultado_final
    conta = 11
    resultado = 0

    cpf_dez_dig = str(cpf_dez_dig)

    for numero in cpf_dez_dig:
        resultado += conta * int(numero)
        conta -= 1

   

    conta = (resultado * 10) % 11
    resultado_final2 = 0 if conta > 9 else conta

    cpf_gerado_conta = f'{cpf_nove_dig}{resultado_final}{resultado_final2}'

    print(f'{cpf_nove_dig}{resultado_final}{resultado_final2}')




        


