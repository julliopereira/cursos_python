### UM LAÇO PARA PEDIR INGREDIENTES PARA UMA PIZZA COM quit PARA SAIR
### INGREDIENTE ESCOLHIDO APRENSENTAR NA TELA

ingr = ''

print('Digite os ingredientes para a pizza: \n')


while ingr != 'quit':
    ingr = input('\tIngrediente: ')
    if ingr == 'quit':
        break

print('Ótimo pedido, estamos preparando sua pizza...')
