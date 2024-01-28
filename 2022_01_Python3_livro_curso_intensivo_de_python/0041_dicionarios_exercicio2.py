### UM LAÇO QUE PERCORRE AS CHAVES E AS EXIBE
print('-'*50)

esportes = {
    'fabio': 'futebol',
    'pedro': 'futebol',
    'silvia': 'voley',
    'eduardo': 'basquete',
    'marcio': 'handbol',
    'sara': 'voley',
    'clebio': 'golf',
    'maria': 'bike',
    'felipe': 'tiro',
    'bruno': 'tiro',
    'lucas': 'arco',
    }

for key, value in esportes.items():
    print(key + ':' +  value)


### MOSTRE APENAS OS NOMES DE TODOS OS PARTICIPANTES SEM REPETÍ-LOS SE HOUVER DUPLICIDADE
print('-'*50)

print('VEJA QUE O TIPO DE ESPORTE NÃO SE REPETE: \n')
for value in sorted(set(esportes.values())):       # sorted (em ordem) set (unificar) values (mostra apenas do campo values)
    print(value)


### CRIE UM DICIONÁRIO QUE CONTRANHA O NOME DE TRÊS RIOS IMPORTANTES E O PAÍS QUE O RIO CORTA
### USE UM LAÇO COM UMA FRASE PARA CADA RIO DIZENDO QUAL PAIS PERCORRE
print('-'*50)

rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'jordão': 'israel',
    }

for key, value in rios.items():
    print('O rio ' + key.title() + ' corre pelo país ' + value .title()+ '.\n')