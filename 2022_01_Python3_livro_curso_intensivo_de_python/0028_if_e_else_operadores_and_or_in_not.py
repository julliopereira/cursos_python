### TESTANDO DUAS CONDIÇÕES COM AND QUE EXIJE QUE AMBAS COMPARAÇÕES SEJAM VERDADEIRAS PARA RETORNAR True/Verdadeiro

idade_0 = 21
idade_1 = 50

if idade_0 <= 21 and idade_1 <= 50: 
    print('Você é maior de idade mas não é velho')

print('-'*50)
if idade_0 == 22 or idade_1 <= 50:
    print('Você ainda não é velho')


### É POSSÍVEL USAR TAMBÉM parenteses () PARA SIMBOLIZAR OU MOSTRAR DE FORMA MAIS EXPLICITA O QUE SE QUER FAZER
print('-'*50)
if (idade_0 == 22) or (idade_1 <= 50):          # AQUI ESTAMOS UTILIZANDO OS () EM CADA COMPARAÇÃO
    print('Você ainda não é velho')


### SE UM VALOR ESTÁ DENTRO DE UMA LISTA OU VARIAVEL usando ' in '
print('-'*50)
carros = ['ford', 'gm', 'volks', 'audi']
if 'audi' in carros: 
        print('Achei "audi" na lista')


### SE UM VALOR NÃO ESTÁ DENTRO DE UMA LISTA OU VARIAVEL usando ' not in '
print('-'*50)
carros = ['ford', 'gm', 'volks', 'audi']
if 'bmw' not in carros: 
        print('BMW não está nalista.')

