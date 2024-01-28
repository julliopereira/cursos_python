### CRIAR UMA LISTA admin COM 5 USUARIOS

usuarios = ['maria', 'paulo', 'silvia', 'admin', 'joao', 'ciro', 'jose']

### ESCREVER UMA SAUDAÇÃO PARA CADA USUÁRIO APÓS LOGIN
print('-'*50)
for usuario in usuarios:
    print('\nSenhor(a) "' + str(usuario).title() + '" loggin realizado! \n')

### SE O USUÁRIO FOR admin EXIBA MENSAGEM ESPECIAL SE NÃO MOSTRE MENSAGEM COMUM AOS DEMAIS COM else
print('-'*50)
login = 'admin'

for usuario in usuarios:
    if login.lower() in usuario:
        print('\nOlá senhor "' + str(usuario).title() + '" gostaria de ver um relatório de status? ... \n' )
    else:
        print('\nSenhor(a) "' + str(usuario).title() + '" loggin realizado! \n')


del usuarios
### VERIFICAR SE A LISTA TEM NOME DE USUARIO IGUAL
### CRIE UMA LISTA CHAMADA current_users COM CINCO OU MAIS NOMES 
print('-'*50)

current_users = ['maria', 'paulo', 'silvia', 'admin', 'joao', 'ciro', 'jose']
new_users =  ['selma', 'samanta', 'sara', 'silvio', 'joao', 'paulo']

### PERCORRER A LISTA new_users PARA VERIFICAR SE OS USUARIOS JÁ FORAM UTILIZADOS EM current_users

for user in new_users:
    if user.lower() in current_users:  # USUARIO John ou JOHN ou john SAO A MESMA COISA
        print('Usuário "' + str(user) + '" existente, troque de usuário. \n')



### CRIE UMA LISTA DE NUMEROS 
print('-'*50)

numeros = list(range(1, 9+1))

### USE UM for PARA PERCORRER E if PARA MOSTRAR OS NUMEROS ORDINAIS
for numero in numeros:
    if numero == 1:
        print( str(numero) + 'st')
    elif numero == 2:
        print( str(numero) + 'nd')
    else:
        print( str(numero) + 'th')
