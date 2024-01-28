"""
Introdução às funções (def) em Python 
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

# exemplo 1
# def imprimir(a, b, c):
#     print(c, b, a)
#     print(c,)
#     print(c, b)
#     print(b, a)

# imprimir(1, 2 , 3)
# imprimir(17, 8 , 13)
# imprimir(13, 22 , 32)
# imprimir(166, 26 , 63)
# imprimir(71, 27 , 73)
# imprimir(91, 29 , 39)

# exemplo2
# def saudacao(nome):
#     print(f'Ola, {nome}!')

# saudacao('Luiz otavio')
# saudacao('Julio')

# exemplo3
def saudacao(nome='sem nome'):      # se nao passar valor ele atribui 'sem nome' a variavel nome
    print(f'Ola, {nome}!')

saudacao('Luiz otavio')
saudacao('Julio')
saudacao()