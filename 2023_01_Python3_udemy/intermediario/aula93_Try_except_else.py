# Try, except, else e finally

# a = 18
# b = 0

try:
    a = 18
    b = 0  
    c = a / b

except ZeroDivisionError:
    print(f'\n\ta não é divisível por b')

except NameError:
    print(f'Não digitou a ou b')

except (TypeError, IndexError):     # abrir uma tupla para tratar duas exceções em um except
    print(f'TypeError e IndexError')

except Exception:                   # ultima classe de erro
    print(f'Erro Desconhecido.')

print('\n\nCONTINUAR')