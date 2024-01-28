# VAMOS USAR json.dump() e json.load() NO MESMO ARQUIVO PARA RECUPERAR O NOME DIGITADO, REFATORACAO

import json

def greet_user():
    """Saúda o usuário pelo nome"""
    filename = input('Digite seu username: ')
    try:
        with open(filename) as f_obj:                          # GRAVA NOME DO ARQUIVO EM f_obj
            username = json.load(f_obj)                        # CARREGA O CONTEUDO DE f_obj NA VARIAVEL USERNAME 
    except FileNotFoundError:                                  # EXECUTA O BLOCO ABAIXO SE O ARQUIVO NAO EXISTIR
        username = input('Qual o seu username: ')              # PEDE AO USUARIO UM USERNAME
        with open(filename, 'w') as f_obj:                     # ABRE O ARQUIVO EM MODO DE GRAVAÇÃO
            json.dump(username, f_obj)                         # GRAVA O CONTEUDO DA VARIAVEL username EM f_obj
            print(f'\n\tNós relembraremos você "{username}".') 
    else:
        print(f'\n\tBem vindo de volta "{username}"!')         # SE O ARQUIVO EXISTIR EM try ENTAO RELEMBRA O username

greet_user()