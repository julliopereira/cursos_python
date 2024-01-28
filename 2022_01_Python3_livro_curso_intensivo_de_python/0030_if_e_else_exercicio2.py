### EXERCICIO DO LIVRO

# CRIAR VARIÁVEL alien_color COM COR

alien_color = 'green'

# ESCREVER if PARA TESTAR SE A COR É VERDE E DAR PONTOS SE SIM

if alien_color == 'green':
    print('Parabéns a cor é verde e você ganhou 10 pontos')

# ESCREVA UMA VERSÃO QUE FALHE 
print('-'*50)

alien_color = 'blue'

if alien_color == 'green':
    print('Parabéns a cor é verde e você ganhou 10 pontos')


# ESCOLHER UMA COR PARA UM ALIENIGENA ESCREVENDO UMA CADEIA If e else
print('-'*50)

if alien_color == 'green':
    print('O valor é verde')
else:
    print('O valor é ' + alien_color)

# ALTERANDO O CODIGO ACIMA PARA QUE TENHA if , elif e else
print('-'*50)

if alien_color == 'green':
    print('A cor é green')
elif alien_color == 'red':
    print('A cor é red')
else:
    print('A cor é: ' + alien_color)
