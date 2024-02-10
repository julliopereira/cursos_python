# Funcoes recursivas e recursividade
# - funcoes que podem se chamar de volta
# - uteis p/ dividir problemas grandes em partes menores
#Toda funcao recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema 
# - Um caso base que para a recursão
# - fatorial -m! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recursiva(inicio=0, fim=4):
    # caso base
    if inicio >= fim:
        return fim 


    # caso recursivo
    # contar at[e chegar ao final
    inicio += 1 
    return recursiva(inicio,fim)

print(recursiva())
