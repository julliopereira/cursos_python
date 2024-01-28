### SE PUDESSE CONVIDAR ALGUEM VIVO OU MORTO PARA JANTAR, QUEM CONVIDARIA?
### CRIE UMA LISTA QUE INCLUA PELO MENOS TRÊS PESSOAS QUE GOSTARIADE CONVIDAR PARA JANTAR.
### EM SEGUIDA UTILIZE A LISTA PARA EXIBIR UMA MENSAGEM PARA CADA PESSOA, CONVIDANDO-A PARA JANTAR.

convidados = ['nicola tesla', 'platão', 'jesus', 'gengiskan', 'isac newton']
print('Convite para ' + convidados[0] + ' para jantar')
print('Convite para ' + convidados[1] + ' para jantar')
print('Convite para ' + convidados[2] + ' para jantar')
print('Convite para ' + convidados[3] + ' para jantar')
print('Convite para ' + convidados[4] + ' para jantar')


print('-'*50)
### UM DOS CONVIDADOS NÃO PODERÁ COMPARECER, MONTE OUTRA LISTA COM OUTRO CONVIDADO:

print('O convidado ' + convidados[3] + ' náo poderá comparecer, vou convidar o caligola')
convidados[3] = 'caligola'
print('Convite para ' + convidados[0] + ' para jantar')
print('Convite para ' + convidados[1] + ' para jantar')
print('Convite para ' + convidados[2] + ' para jantar')
print('Convite para ' + convidados[3] + ' para jantar')
print('Convite para ' + convidados[4] + ' para jantar')

### CONVIDE MAIS TRÊS PESSOAS PARA JANTAR
print('-'*50)
print(convidados)
print('Encontrei uma mesa maior para jantar, vou convidar mais três pessoas...')
convidados.append('tutancamon')
convidados.append('cleopatra')
convidados.append('D. pedro I')
print(convidados)
print('Convite para ' + convidados[5] + ' para jantar')
print('Convite para ' + convidados[6] + ' para jantar')
print('Convite para ' + convidados[7] + ' para jantar')

### CONVIDE MAIS 3 PESSOAS MAS ADICIONE EM LOCAIS DIFERENTES NA SUA LISTA, POSICAO: 0,4,6
print('-'*50)
print(convidados)
print('Adicionando mais três pessoas na lista')
convidados.insert(0, 'josé')
convidados.insert(4, 'joão')
convidados.insert(6, 'herodes')
print(convidados)
print('Convite para ' + convidados[0] + ' para jantar')
print('Convite para ' + convidados[4] + ' para jantar')
print('Convite para ' + convidados[6] + ' para jantar')

### A MESA DE JANTAR MAIOR NÃO CHEGARÁ, PRECISO REDUZIR O NUMERO DE CONVIDADOS PARA 2
print('-'*50)
print(convidados)
print('Peço desculpas aos senhores... \n' + str(convidados) + '\n mas não poderei convidar todos, o convite está cancelado')
#for i in range(len(convidados)):"
for i in range(10, -1, -1):    
    convidado = convidados.pop(i).title()
    print('Atenção senhor(a) "' + convidado + '" o convite feito para jantar foi cancelado')
print('Após deleção da lista:',convidados)
print('Criando nova lista...')
convidados = ['jesus', 'josé']
print('Novo convite para "' + convidados[0].title() + '" para jantar')
print('Novo convite para "' + convidados[1].title() + '" para jantar')

### APAGANDO A LISTA APÓS JANTAR
print('-'*50)
print('obrigado aos senhores ', convidados)
print('Apagando a lista...')
del convidados


