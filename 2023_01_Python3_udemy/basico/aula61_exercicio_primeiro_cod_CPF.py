
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

# cpf = input('Digite um CPF(somente numeros): ')
cpf = '77833556092'

cpf_nove_dig = cpf[:9]
soma = 0
conta = 10

for numero in cpf_nove_dig:
    resultado = conta * int(numero)
    soma = soma + resultado
    conta -= 1

print(f'1total: {soma}')

multiplica_por_dez = soma * 10
conta = multiplica_por_dez % 11

resultado_final = 0 if conta > 9 else conta
print(f'Primeiro Digito igual a: {resultado_final}')

cpf_dez_dig = cpf[:10]
conta = 11
resultado = 0

for numero in cpf_dez_dig:
    resultado += conta * int(numero)
    conta -= 1

print(f'2total: {resultado}')

conta = (resultado * 10) % 11
print(conta)
resultado_final2 = 0 if conta > 9 else conta
print(f'Segundo Digito igual a: {resultado_final2}')

cpf_gerado_conta = f'{cpf_nove_dig}{resultado_final}{resultado_final2}'

if cpf_gerado_conta == cpf:
    print('CPF válido')
else:
    print('CPF inválido')




    


