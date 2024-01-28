""" 
Interpolacao basica de string
s       - string
d e i   - int
f       - float
x e X   - Hexadecimal (ABCDEF0123456789)
""" 

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.3f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))
print('O hexadecimal de %d é %08x' % (15, 15))
print('O hexadecimal de %d é %04X' % (15, 15))