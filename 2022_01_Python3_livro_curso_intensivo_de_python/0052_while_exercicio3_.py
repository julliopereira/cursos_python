### USAR TUDO QUE FOI APRENDIDO

ingr = ''

print('Digite os ingredientes para a pizza: \n')


while ingr != 'quit':
    ingr = input('\tIngrediente: ')
    if ingr == 'quit':
        break

while True:
    cartao = input('Como deseja pagar ?')
    if cartao != '':
        break
    else:
        continue

print('\n\nÓtimo pedido, estamos preparando sua pizza...')
print('Pagamento com cartao: ' + cartao)