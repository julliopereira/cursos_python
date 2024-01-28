
"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

# exemplo 1
# print('valor' if False else 'Outro valor')

# exemplo 2
# condicao = 10 == 100
# variavel = 'Valor' if condicao else 'Outro valor' # Mostra 'Valor' se condicao verdadeira senao 'Outro valor'
# print(variavel)

# exemplo 3
# digito = 9
# novo_digito = digito if digito <= 9 else 0
# print(novo_digito)

# exemplo 4
# digito = 9
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

# exemplo 5
print('Valor' if False else 'Outro Valor' if False else 'Fim')


