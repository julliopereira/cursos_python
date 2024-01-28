# O USUARIO VAI DAR SEU NOME AO INICIAR O PROGRAMA 
# O PROGRAMA VAI LEMBRAR O NOME DO USUARIO QUANDO ENTRAR NOVAMENTE

import json
username = input('Qual o seu username: ')
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print(f'\n\tNós iremos relembrar seu nome "{username}"')