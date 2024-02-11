# Funcoes recursivas e recursividade
# - funcoes que podem se chamar de volta
# - uteis p/ dividir problemas grandes em partes menores
#Toda funcao recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema 
# - Um caso base que para a recursão
# - fatorial -m! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# import sys

# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=4):

#     print(inicio, fim)

#     # caso base
#     if inicio >= fim:
#         return fim 


#     # caso recursivo
#     # contar at[e chegar ao final
#     inicio += 1 
#     return recursiva(inicio,fim)

# print(recursiva(0, 995))

# --------------------------------------


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


