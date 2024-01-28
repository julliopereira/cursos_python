# list comprehension é uma forma rápida para criar listas a partir de iteraveis
#
# print(list(range(10)))

# ex1: python inclua o numero que está na variável numero usando range de 10
lista = [numero for numero in range(1,10)]
print(lista)

lista.clear()

# ex2: mesma coisa de outra forma
lista = [
    numero * 2 
    for numero in range(10)
]
print(lista)