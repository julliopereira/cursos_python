mario = { 
    'nome': 'mario',
    'sobrenome': 'ayala',
    'altura': '1.80',
    'peso': '80',
    'civil': 'solteiro',
    'esporte': 'futebol',
    'trabalho': 'engenheiro',
    }

maria = { 
    'nome': 'maria',
    'sobrenome': 'mendes',
    'altura': '1.65',
    'peso': '60',
    'civil': 'solteira',
    'esporte': 'voley',
    'trabalho': 'tecnica',
    }

julio = { 
    'nome': 'julio',
    'sobrenome': 'pereira',
    'altura': '1.84',
    'peso': '90',
    'civil': 'solteiro',
    'esporte': 'futebol',
    'trabalho': 'Adm de rede',
    }

pessoas = [mario,maria,julio]
for pessoa in pessoas:
    print('\nAs informações de ' + pessoa['nome'] + ' são:\n')
    for k, v in pessoa.items():
        print('\t' + k + ':' + v)


