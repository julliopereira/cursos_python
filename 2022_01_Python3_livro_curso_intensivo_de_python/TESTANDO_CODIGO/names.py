from name_function import get_formated_name
print('Entre com "q" qualquer hora para sair!')

while True:
    first = input('\nPor favor me de o primeiro nome: ')
    if first == 'q':
        break
    last = input('Por favor me de seu ultimo nome: ')
    if last == 'q':
        break

    formatted_name = get_formated_name(first,last)
    print(f'\n\tNome ordenado "{formatted_name}."')