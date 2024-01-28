### 5 LUGARES DO MUNDO QUE GOSTARIA DE VISITAR:
### CERTIFIQUE DE MONTAR A LISTA FORA DE ORDEM ALFABETICA
### EXIBA A LISTA NA FORMA ORIGINAL
### UTILIZE sorted() PARA EXIBIR SUA LISTA EM ORDEM ALFABETICA SEM MODIFICAR A LISTA
### MOSTRE QUE A LISTA MANTEVE A ORDEM ORIGINAL 
### UTILIZE sorted() PARA EXIBIR A LISTA INVERSA SEM ALTERAR A ORDEM ORIGINAL
### MUDAR ORDEM DA LISTA (ultimo seja o primeiro e o primeiro o ultimo) E MOSTRE
### INVERTA NOVAMENTE E MOSTRE
### USE sort() PARA ALTERAR A LISTA EM ORDEM ALFABETICA DE FORMA PERMANENTE E MOSTRE
### USE sort() PARA ALTERAR A LISTA EM ORDEM ALFABETICA INVERSA PERMANENTE E MOSTRE

lugares = ['k2', 'aconcágua','magino', 'zigurate', 'machu picho'] 
print(lugares)
print(sorted(lugares))
print(lugares)
print(sorted(lugares, reverse=True))
print(lugares)
lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=True)
print(lugares)

### CRIE UMA LISTA DE JANTAR E USE len() PARA MOSTRAR O NUMERO DE CONVIDADOS QUE ESTA CONVIDANDO
 
print('-'*50)
convidados = ['maria', 'jose', 'joao', 'jesus', 'pedro', 'paulo']
print(len(convidados))

### CRIE UMA LISTA GRANDE DE QUALQUER ASSUNTO QUE QUEIRA E DEPOIS MOSTRE CADA UMA

print('-'*50)
paises = ['brasil', 'espanha', 'camboja', 'usa', 'argentina', 'chile', 'alemanha', 'panama', 'mexico', 'canada', 'guiana', 'peru', 'franca', 'iran', 'russia', 'china', 'grecia', 'ruanda', 'kenia', 'egito', 'israel']
for c in paises:
    print('Gostaria de ir para o país "' + c + '"\t para fazer turismo.')