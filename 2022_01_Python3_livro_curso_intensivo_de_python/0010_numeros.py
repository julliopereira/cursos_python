
### EXISTEM 2 TIPOS DE NUMEROS
'''
descrição                 valor   tipo
NUMEROS INTEIROS        = 234   = int
NUMEROS PONTO FLUTUANTE = 2.34  = float
'''


### PODE UTILIZAR AS OPERACOES somar(+), subtrair(-), multiplicar(*), dividir(/) INTEIROS EM PYTHON:

print('3 + 2\t\t',3 + 2)
print('3 - 2\t\t',3 - 2)
print('3 * 2\t\t',3 * 2)
print('3 / 2\t\t',3 / 2)

print('-'*50)
### DEVOLVE O RESULTADO DA OPERACAO. DOIS SIMBOLOS REPRESENTAM EXPONENCIAÇÃO:

print('3^2 \t\t',3 ** 2)
print('3^3:\t\t',3 ** 3)
print('10^6:\t\t',10 ** 6)

print('-'*50)
### ORDENAR OPERAÇÕES (QUAL SERÁ EXECUTADA PRIMEIRO)

print('2 + (3 * 4):\t', 2 + (3*4))
print('(2 + 3) * 4:\t', (2 + 3) * 4)

print('-'*50)
### CALCULOS COM NUMEROS DE PONTO FLUTUANTE

print('0.1 + 0.1:\t', 0.1 + 0.1)
print('0.2 + 0.2:\t', 0.2 + 0.2)
print('2 * 0.1:\t', 2 * 0.1)
print('2 * 0.2:\t', 2 * 0.2)

print('-'*50)
### CUIDADO POIS PODE RETORNAR NUMEROS ENORMES, O PYTHON PODE CORRIGIR ISSO, IGNORANDO CASAS DECIMAIS A DIREITA:

print('0.2 + 0.1:\t', 0.2 + 0.1)        # SERÁ APRESENTANDO COMO REDUZIR MAIS A FRENTE
print('3 * 0.1:\t', 3 * 0.1)            # SERÁ APRESENTANDO COMO REDUZIR MAIS A FRENTE


print('-'*50)
### MODULO % REALIZA OPERACÃO DE DIVISÃO E RETORNA O RESTO:

print('5 % 3:\t', 5 % 3)
