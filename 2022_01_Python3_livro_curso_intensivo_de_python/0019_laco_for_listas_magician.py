### LAÇO for - MOSTRA OS 3 NOMES NA LISTA EM UM LOOP 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())

'''
BOAS PRÁTICAS:
para listas utilizar nome da variavel que tenha relação com o conjunto 
gatos
cachorros
lista_de_itens

e a variavel do for utilizar no singular

gato
cachorro
item
'''

### LAÇO for - INTENÇÃO É QUE TODOS RECEBAM A MENSAGEM DE REPETIÇÃO DE MAGICA, MAS PELA IDENTAÇÃO SOMENTE O ULTIMO MAGICO RECEBERA O PEDIDO
### O PROGRAMA RODA SEM PROBLEMA DE LÓGICA NO ENTANTO NÃO APRESENTA O RESULTADO QUE ESPERAMOS
print('-'*50)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print('Uau "' + magician.title() + '" excelente mágica')
print('\t- Poderia repetir a mágica ?')


### LAÇO for - INTENÇÃO É QUE TODOS RECEBAM A MENSAGEM DE REPETIÇÃO DE MAGICA
### ALTERANDO A IDENTAÇÃO PODEMOS OBTER O RESULTADO ESPERADO
print('-'*50)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print('Uau "' + magician.title() + '" excelente mágica')
    print('\t- Poderia repetir a mágica ?\n')                        # < ALTERADO IDENTAÇÃO
print('Obrigado a TODOS os mágicos pela apresentação !!!')