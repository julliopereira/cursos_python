# VAMOS ALTERAR A nacionalidade PARA ingles MUDAR OS PONTOS PARA 10 E A VELOCIDADE PARA fast

pessoas = []                                         # LISTA VAZIA

for pessoa in range(30):                             # O range() gera 30 ocorrencias 
    nova_pessoa = {                                  # Então é criado um dissionário com 3 x chaves-valores
        'nacionalidade': 'japones', 
        'pontos': 5, 
        'velocidade': 'slow',
        }
    pessoas.append(nova_pessoa)                      # Então adicionamos à lista pessoas exatamente o dissionário criado 

for pessoa in pessoas[:3]:                           # Vai mostrar as 5 primeiras ocorrências da lista
    if pessoa['nacionalidade'] == 'japones':
        pessoa['nacionalidade'] = 'ingles'
        pessoa['pontos'] = 10
        pessoa['velocidade'] = 'fast'
 
for pessoa in pessoas[:5]:                           # Mostrar as 5 primeiras ocorrencias (verificar que as 3 primeiras foram alteradas)
    print(pessoa)       

print('-'*50) #---------------------------------------------------------------------------------------

print('Todal de pessoas: ' + str(len(pessoas)))      # Mostra a quantidade de pessoas

