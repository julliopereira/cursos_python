"""
Repeticoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quanto um código não tem fim 
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o',contador)
        continue

    if contador >= 17 and contador <= 24 :
        print('Não vou mostrar o',contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')