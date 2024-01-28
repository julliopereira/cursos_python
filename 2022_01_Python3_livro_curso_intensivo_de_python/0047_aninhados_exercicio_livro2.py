### CRIAR UM DICIONARIO ONDE NOME DOS DICIONARIOS SÃO OS NOMES DOS PETS
### EM CADA DICIONARIO INCLUA O TIPO DO ANIMAL E NOME DO DONO
### ARMAZENE EM UMA LISTA CHAMADA PETS
### PERCORRER LISTA COM LAÇO MOSTRANDO INFORMAÇÕES

cachorro = {
        'tipo': 'mamifero',
        'dono': 'mario',
    }

cavalo = {
        'tipo': 'equino',
        'dono': 'pedro',
    }

cobra = {
        'tipo': 'reptil',
        'dono': 'lara',
    }

pets = [cachorro, cavalo, cobra]

for pet in pets:
    for key, value in pet.items():
        print(key + ':\n\t' + value + '\n')


