"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escobo global e local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem 
ser alcançados.não temos acesso a nomes de escopos internos nos escopos externos. 
A palavra global faz uma vari[avel do escpo externo ser a mesma no escopo interno
"""

# exemplo 1

# AMBIENTE GLOBAL

# def escopo():
#     # AMBIENTE LOCAL
#     x = 1           # X está definido dentro da função
#     print(x)

# print(x)            # X está definido dentro da função (erro)

# escopo()

#--------------------------------------
# exemplo 2
# x = 1

# def escopo1():
#     x = 2
#     def escopo2():
#         x = 3
#         y = 3
#         print(f'x + y do escopo 2: {x + y}')
#     print(f'x do escopo 1: {x}')
#     escopo2()                                   # chamando funcao escopo2 dentro da funcao escopo1

# escopo1()                                       # chamando funcao escopo1

# print(f'x de global: {x}')

#--------------------------------------

# exemplo 3
x = 1

def escopo1():
    global x                                    # informa que vai alterar o x global
    x = 2
    def escopo2():
        x = 3
        y = 3
        print(f'x + y do escopo 2: {x + y}')
    print(f'x do escopo 1: {x}')
    escopo2()                                   # chamando funcao escopo2 dentro da funcao escopo1

escopo1()                                       # chamando funcao escopo1

print(f'x de global: {x}')
