### FAÇA VOCE MESMO

# CRIAR DOIS NOVOS DICIONARIOS QUE  REPRESENTEM PESSOAS DIFERENTE E ARMAZENE EM UM DICIONARIO
# ARMAZENE OS TRES DICIONARIOS EM UMA LISTA CHAMADA people. PERCORRA SUA LISTA DE PESSOAS COM UM LAÇO.
# A MEDIDA QUE PERCORRER A LISTA APRESENTE TUDO QUE VOCÊ SABE SOBRE CADA PESSOA




pessoas = { 
    'username_mario' : { 
        'nome': 'mario',
        'sobrenome': 'ayala',
        'altura': '1.80',
        'peso': '80',
        'civil': 'solteiro',
        'esporte': 'futebol',
        'trabalho': 'engenheiro',
        },

    'username_maria' : { 
        'nome': 'maria',
        'sobrenome': 'mendes',
        'altura': '1.65',
        'peso': '60',
        'civil': 'solteira',
        'esporte': 'voley',
        'trabalho': 'tecnica',
        },

    'username_julio' : { 
        'nome': 'julio',
        'sobrenome': 'pereira',
        'altura': '1.84',
        'peso': '90',
        'civil': 'solteiro',
        'esporte': 'futebol',
        'trabalho': 'Adm de rede',
        },
    }

dicionarios = [pessoas]

for dicionario in dicionarios:
    for username, nome_info in pessoas.items():  # username = nome dos dicionarios internos| nome_info = valores dentro de cada dissionario 
        print('\nO seu username é: ' + username)
        nome_sobrenome = nome_info['nome'] + " " + nome_info['sobrenome']
        massa = nome_info['peso']

        print('\t' + nome_sobrenome.title())
        print('\t' + massa.title())
