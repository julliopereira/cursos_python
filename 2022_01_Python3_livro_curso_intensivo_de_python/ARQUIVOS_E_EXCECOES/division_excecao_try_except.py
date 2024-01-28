# try-except = bloco para tratar EXCEÇÕES que nada mais é que erro em Python. 

try:
    print(5/0)                                                      # EXECUTE CONTA 5/0
except ZeroDivisionError:
    print('Você não pode dividir qualquer número por zero!!!')      # MOSTRE ESSA MSG SE DIVIDIR POR ZERO

# SE HOUVER MAIS CÓDIGOS APÓS A EXCEÇÃO TRATADA O PROGRAMA CONTINUARÁ SENDO EXECUTADO

print('\n\tcontinuação do código ...')
