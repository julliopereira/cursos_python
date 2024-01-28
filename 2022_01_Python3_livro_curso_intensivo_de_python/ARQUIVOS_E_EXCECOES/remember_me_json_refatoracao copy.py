# VAMOS USAR json.dump() e json.load() NO MESMO ARQUIVO PARA RECUPERAR O NOME DIGITADO, REFATORACAO

import json

def get_stored_username():
    """Obtem o nome ja armazenado se estiver disponviel"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:                          
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username 

def greet_user():
    """Saúda o usuário pelo nome"""
    username = get_stored_username()
    if username:
        print(f'Bem vindo de volta "{username}"')
    else:
        username = input('Qual o seu username: ')              # PEDE AO USUARIO UM USERNAME
        filename = 'username.json'
        with open(filename, 'w') as f_obj:                     # ABRE O ARQUIVO EM MODO DE GRAVAÇÃO
            json.dump(username, f_obj)                         # GRAVA O CONTEUDO DA VARIAVEL username EM f_obj
            print(f'\n\tNós relembraremos você "{username}".') 

greet_user()