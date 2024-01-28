### REMOVENDO ESPAÇOS EM BRANCO 
### ESPAÇOS EM BRANCO MUITAS VEZES SÃO DIGITADOS PELO USUÁRIO E PRECISAMOS ENTÃO REMOVE-LOS

'''
'Python'        # sem espaço
'Python '       # com espaço no final 
' Puthon     '  # com espaço no começo e no final 
'''

linguagem = 'python '
linguagem = linguagem.rstrip()              # removendo espaços a direita
print(linguagem)

print('-'*20)
linguagem = '  python'
print(linguagem)
linguagem = linguagem.lstrip()              # removendo espaços a esquerda
print(linguagem)

print('-'*20)
linguagem = '  python                               '
print(linguagem)
linguagem = linguagem.strip()              # removendo espaços a esquerda e direita
print(linguagem)
