### USANDO LISTAS DENTRO DE DICIONARIOS

linguagens_favoritas = {                            # CRIAR DISSIONARIO ONDE OS values SÃO LISTAS
    'joao': ['python', 'c'],
    'sara': ['c'],
    'eduardo': ['ruby', 'java'],
    'jorge': ['python'],
    }

for nome, linguagem in linguagens_favoritas.items():                        # UM FOR PARA BUSCAR keys E values
    if len(linguagem) > 1:                                                  # SE O TAMANHO DA LISTA FOR MAIOR QUE 1 ITEM 
        print(nome.title() + ', as linguagens que você escolheu são: ')         # NO PLURAL
        for ling in linguagem:                                  
            print('\t',ling)
            
    elif len(linguagem) == 1:                                               # SE O TAMANHO DA LISTA FOR IGUAL A 1 ITEM 
        print(nome.title() + ', a linguaguem que você escolheu é: ')            # NO SINGULAR
        for ling in linguagem: 
            print('\t',ling)
    