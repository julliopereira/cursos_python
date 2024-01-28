# try, except, else e finally

try:
    print(1)
    10 / 0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

else:                                   # não ocorreram exceções 
    print('Não ocorreram erros')
finally:                                # sempre será executado mesmo se ocorrer erro
    print(2)

