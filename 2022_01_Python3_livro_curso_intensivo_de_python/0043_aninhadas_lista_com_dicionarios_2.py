# AQUI VAMOS AGORA MONTAR ALGO PARECIDO PORÉM COM 30 PESSOAS

pessoas = []                                         # LISTA VAZIA

for pessoa in range(30):                             # O range() gera 30 ocorrencias 
    nova_pessoa = {                                  # Então é criado um dissionário com 3 x chaves-valores
        'nacionalidade': 'japones', 
        'pontos': 5, 
        'velocidade': 'slow',
        }
    pessoas.append(nova_pessoa)                      # Então adicionamos à lista pessoas exatamente o dissionário criado 

for pessoa in pessoas[:5]:                           # Vai mostrar as 5 primeiras ocorrências da lista
    print(pessoa)


print('-'*50) #---------------------------------------------------------------------------------------

print('Todal de pessoas: ' + str(len(pessoas)))      # Mostra a quantidade de pessoas
