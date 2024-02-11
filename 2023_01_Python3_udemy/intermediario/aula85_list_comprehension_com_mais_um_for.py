lista = [ ]
for x in range(3): 
    for y in range(3):
        lista.append((x,y))
# mesma coisa do de cima
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
# mesma coisa 
lista = [ 
    [x for y in range(3)]
    for x in range(3)
]

print(lista)