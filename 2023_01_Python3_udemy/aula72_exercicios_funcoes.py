# funcao que multiplica todos os argumentos
# nao nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável. 

# Crie uma função que retorna se numero é par ou ímpar

def multiplica(*args):
    total = 0
    for numero in args:
        if total == 0:
            total = numero
        else:
            total *= numero
    return total 

def retorna_par_ou_impar(x):
    if x % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'
    
multiplicado = multiplica(1,3,7)
par_impar = retorna_par_ou_impar(multiplicado)

print(f'Resultado da multiplicação é: "{multiplicado}" e o valor é: "{par_impar}"')

