import os

"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_de_compras = ['maca', 'pera', 'tomate', 'cafe', 'biscoito']

while True:

    os.system('clear')
    print(f'Selecione uma opcão:')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        indice_inserir = input('\tDigite nome do item a ser inserido: ')
        lista_de_compras.append(indice_inserir)
        
    elif opcao == 'a':
        try:
            indice_apagar = int(input('\tQual indice devo apagar: '))
            lista_de_compras.pop(indice_apagar)
        except ValueError:
            print('Deve digitar um numero!! \n')
            input(f'\nDigite <enter> para continuar...')
        except IndexError:
            print('Indice não existe na lista \n')
            input(f'\nDigite <enter> para continuar...')
        except Exception:
            print('Erro desconhecido !! \n')
            input(f'\nDigite <enter> para continuar...')            
    
    elif opcao == 'l':
        for indice, valor in enumerate(lista_de_compras):
            print(indice, valor)
        input(f'\nDigite <enter> para continuar...')

    else:
        print('Letra incorreta digitar "i" , "a" , "l"')