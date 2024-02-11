# Generator expression, Iterables e Iterators em Python
# iterator = entrega valor por valor, sempre o próximo valor

import sys      # modulo para verificar tamanho da lista em bytes

iterable = ['Eu', 'Tenho', '__iter__']
iterator =  iter(iterable)        # mesmo: iterable.__iter__()  # tem __iter__ e __next__
lista = [n for n in range(100000)]      # uma lista
generator = (n for n in range(100000))  # uma tupla

print(generator)                # mostra que que o objeto foi salvo na memoria xyz
print(sys.getsizeof(lista))     # mostra tamanho da lista salva na memoria do computador
print(sys.getsizeof(generator))     # mesmo para generator


for n in generator:
    [print(n) if n == 16 else '']

## nao consigo acessar indice do generator
