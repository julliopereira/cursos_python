# SOMAR OS NUMEROS DAS LISTAS NA QUANTIDADE DA LISTA MENOR

# -MINHA SOLUCAO-
# def calcula(menor, Maior):
#     ...
#     tammen = len(menor)
#     for pos in range(tammen):
#         print(l1[pos] + l2[pos])

# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = [1, 2, 3, 4]

# tl1 = len(l1)
# tl2 = len(l2)

# if tl1 < tl2:
#     calcula(l1, l2)
# else:
#     calcula(l2, l1)

#--------------------------------------

lista_a = [1, 21, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# -SOLUCAO1 - PROFESSOR -

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# -SOLUCAO2 - PROFESSOR -

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# -SOLUCAO3 - PROFESSOR - melhor!!!!!!!!!!!!!!!!!

lista_soma = [x + y for x, y in zip(lista_a,lista_b)]
print(lista_soma)

