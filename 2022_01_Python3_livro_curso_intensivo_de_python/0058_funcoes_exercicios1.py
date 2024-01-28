### PAG 218 

print('EX 1:')

def func_make_shirt(tam):
    print('\n\tO tambanho da camiseta é: ' + tam)

tam = input('\nDigite o tamnho da camiseta: ')
func_make_shirt(tam)

print('-'*50)#------------------------------------------------------------------------------
print('EX 2:')

def func_make_shirt2(texto, tam='G'):
    if tam != '':
        print('\n\tO tamanho da camiseta é: ' + tam)
        print('\n\tO texto da camiseta é: ' + texto)
    else:
        print('\n\tO tamanho da camiseta é: ' + tam)
        print('\n\tO texto da camiseta é: ' + texto)

texto = input('Digite o texto da mensagem: ')
tamanho = input('\nDigite o tamnho da camiseta: ')                      # DEIXE O CAMPO EM BRANCO (DIGITE ENTER) PARA NÃO MANDAR INFORMAÇÃO

func_make_shirt2(texto)

