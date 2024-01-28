### VERIFICAR SE LISTA ESTÁ VAZIA
### SE A LISTA ESTIVER VAZIA ENTÃO O if VAI RETORNAR False E USAR else PARA MOSTRAR MENSAGEM
### SE A LISTA ESTIVER QUALQUER INFORMAÇÃO O if VAI RETORNAR True E USAR if PARA MOSTRAR MENSAGEM

ingredientes = []

if ingredientes:
    for ingrediente in ingredientes:
        print('Adicionando ' + ingrediente + '.\n')
    print('\nFinalizado, fazendo a pizza')
else:
    print('Está certo de que quer uma pizza sem recheio ? \n')


del ingrediente



### AGORA EXCREVER CÓDIGA PARA POPULAR A LISTA
print('-'*50)

ingredientes_disponiveis = ['tomate', 'azeite', 'queijo', 'peperoni', 'ovo', 'anchova']

ingredientes_escolhidos = ['tomate', 'azeite', 'queijo']

if ingredientes_escolhidos:
    for ingrediente in ingredientes_escolhidos:
        print('Adicionando ' + ingrediente + '.\n')
    print('\nFinalizado, fazendo a pizza !! \n')
else:
    print('Está certo de que quer uma pizza sem recheio ?')
