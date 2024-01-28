"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# exemplo de erro (vai gerar um ValueError como exceção)
#print(1234)
#print(456)
#int('a')

# numero_str = input('Vou dobrar o número que você digitar: ')
# numero_str = float(numero_str)                                   # TRATANDO O INPUT DO USUARIO
# print(f'O dobro de {numero_str} é {numero_str * 2:.2f}')         # NESTE CASO É TRATADO UM NUMERO E NAO UM STRING

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print(f'Isso não é um número')




