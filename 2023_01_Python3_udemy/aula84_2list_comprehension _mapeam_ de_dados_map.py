# list comprehension é uma forma rápida para criar listas a partir de iteraveis
#
# print(list(range(10)))

# ex1: python inclua o numero que está na variável numero usando range de 10
# lista = [numero for numero in range(10)]
# print(lista)

# lista.clear()

# # ex2: mesma coisa de outra forma
# lista = [
#     numero * 2 
#     for numero in range(10)
# ]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [ 
    { 'nome': 'p1' , 'preço': 20,},
    { 'nome': 'p2' , 'preço': 10,},
    { 'nome': 'p3' , 'preço': 30,},
]

novos_produtos = [
    # {'nome': produto['nome'], 'preço': produto['preço']} # mapeamento 1
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]
# print(novos_produtos)
print(*novos_produtos, sep='\n')