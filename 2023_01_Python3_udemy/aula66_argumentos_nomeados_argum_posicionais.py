"""
Argumentos nomeados e não nomeados em fuções Python 
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# exemplo 1
def soma(x=0, y=0):
    # Definição
    print(x + y)

soma(1, 8)          # chamando a funcao soma e passando agumentos 1 e 8
soma(y=2, x=1)      # argumentos nomeados


