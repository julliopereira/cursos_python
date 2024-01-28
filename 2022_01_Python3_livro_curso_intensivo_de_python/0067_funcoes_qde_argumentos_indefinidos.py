#### CRIAR UMA FUNÇÃO QUE RECEBA UM NUMEO INDEFINIDO DE ARGUMENTOS

def make_pizza(size, *ingredientes):
    """Apresenta a pizza que estamos prestes a preparar"""
    print('\nFazendo uma pizza taamnho ' + str(size) + ' com os seguintes ingredientes:')
    for ingrediente in ingredientes:
        print('- ' + ingrediente)

make_pizza(17, 'peperoni')
make_pizza(19, 'um queijo', 'dois queijos', 'quatro queijos', 'portuguesa', 'mussarela')